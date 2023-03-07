from scipy import stats
import numpy as np
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import pickle, glob, paths

import seaborn as sns
plt.rcParams['figure.figsize'] = (15, 10)

sns.set_style('ticks')
#sns.set_style('darkgrid')
sns.set_context("talk",font_scale=2,rc={"lines.linewidth": 4,"axes.linewidth": 5})

plt.rc('axes', linewidth=3)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 3
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1.5
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 3
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['ytick.minor.width'] = 1.5
plt.rcParams['axes.edgecolor'] = 'k'#'gray'
#plt.rcParams['axes.grid'] = True
#plt.rcParams['grid.color'] = 'lightgray'
#plt.rcParams['grid.linestyle'] = 'dashed' #dashes=(5, 1)
plt.rcParams['lines.dashed_pattern'] = 10, 3
plt.rcParams['grid.linewidth'] = 1.5
#plt.rcParams['axes.facecolor'] = 'whitesmoke'
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['legend.fancybox'] = True
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.shadow'] = False
plt.rcParams['legend.edgecolor'] = 'lightgray'
plt.rcParams['patch.linewidth'] = 3

#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "Helvetica"
#})

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': 'cmr10',
    'mathtext.fontset': 'cm',
    'axes.formatter.use_mathtext': True # needed when using cm=cmr10 for normal text
})

fig = plt.figure(figsize=(45,7.5))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
axl = plt.subplot(gs[0])
ax1l = plt.subplot(gs[1])
ax2l = plt.subplot(gs[2])
ax3l = plt.subplot(gs[3])
axl.set_ylabel("$\\frac{\Delta\mathrm{[Fe/H]}}{\mathrm{[Fe/H]}(R<2\, \mathrm{kpc})}$")
ax1l.set_yticklabels([])
ax2l.set_yticklabels([])
ax3l.set_yticklabels([])
axl.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax1l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax2l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax3l.set_xlabel("$\mathrm{time\ [Gyr]}$")

axl.set_ylim(-1.25,.45)
axl.set_xlim(0,13.9)
ax1l.set_xlim(0,13.9)
ax1l.set_ylim(-1.25,.45)
ax2l.set_xlim(0,13.9)
ax2l.set_ylim(-1.25,.45)
ax3l.set_xlim(0,13.9)
ax3l.set_ylim(-1.25,.45)

N = 5  # window size for running average of gradient

from matplotlib.pyplot import cm
color = cm.seismic_r(np.linspace(0,1,7))

#let's do g2.79e12

central = []
middle2 = []
middle3 = []
middle = []
outer = []
times = []

time_dict = pickle.load(open(paths.data / '2.79e12_time_dict.dat','rb'))

#file = paths.data / '2.79e12.0????_cold_gas_profile.dat'
gas_profile_files = glob.glob('2.79e12.0????_cold_gas_profile.dat', root_dir=paths.data)
gas_profile_files.sort()

before = time_dict['00320']
after = time_dict['00520']
axl.plot([before,before],[.05,-1.55],color='darkgray')
axl.plot([after,after],[.05,-1.55],color='darkgray')

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(paths.data / f,'rb'))
    # in order to circumvent singularities when enrichment crosses [Fe/H] = 0, we subtract 1 from all values
    # we are anyways only interested in relative deviations.
    cen = np.where((0 < data['bins']) & (data['bins'] < 2))
    mid2 = np.where((3 < data['bins']) & (data['bins'] < 5))
    mid = np.where((7 < data['bins']) & (data['bins'] < 9))
    mid3 = np.where((9 < data['bins']) & (data['bins'] < 13))
    out = np.where((13 < data['bins']) & (data['bins'] < 17))
    central.append(np.mean(data['feh'][cen])-1)
    middle.append(np.mean(data['feh'][mid])-1)
    middle2.append(np.mean(data['feh'][mid2])-1)
    middle3.append(np.mean(data['feh'][mid3])-1)
    outer.append(np.mean(data['feh'][out])-1)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

axl.plot(times[2:-2], -np.convolve((np.asarray(middle2)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid') , label='$3<R<5\, \mathrm{kpc}$', color=color[6])
axl.plot(times[2:-2], -np.convolve((np.asarray(middle)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$7<R<9\, \mathrm{kpc}$', color=color[4])
axl.plot(times[2:-2], -np.convolve((np.asarray(middle3)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$9<R<13\, \mathrm{kpc}$', color='#ff7f0e')#color[2])
axl.plot(times[2:-2], -np.convolve((np.asarray(outer)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$13<R<17\, \mathrm{kpc}$', color=color[1])

axl.set_title('g2.79e12',fontsize=30)
axl.legend(ncol=2, fontsize=27)

# now g8.26e11
central = []
middle2 = []
middle3 = []
middle = []
outer = []
times = []

time_dict = pickle.load(open(paths.data / '8.26e11_time_dict.dat','rb'))

gas_profile_files = glob.glob('8.26e11.0????_cold_gas_profile.dat', root_dir=paths.data)
gas_profile_files.sort()

before = time_dict['00530']
after = time_dict['00710']
ax1l.plot([before,before],[.05,-1.55],color='darkgray')
ax1l.plot([after,after],[.05,-1.55],color='darkgray')

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(paths.data / f,'rb'))
    # in order to circumvent singularities when enrichment crosses [Fe/H] = 0, we subtract 1 from all values
    # we are anyways only interested in relative deviations.
    cen = np.where((0 < data['bins']) & (data['bins'] < 2))
    mid2 = np.where((3 < data['bins']) & (data['bins'] < 5))
    mid = np.where((7 < data['bins']) & (data['bins'] < 9))
    mid3 = np.where((9 < data['bins']) & (data['bins'] < 13))
    out = np.where((13 < data['bins']) & (data['bins'] < 17))
    central.append(np.mean(data['feh'][cen])-1)
    middle.append(np.mean(data['feh'][mid])-1)
    middle2.append(np.mean(data['feh'][mid2])-1)
    middle3.append(np.mean(data['feh'][mid3])-1)
    outer.append(np.mean(data['feh'][out])-1)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

ax1l.plot(times[2:-2], -np.convolve((np.asarray(middle2)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid') , label='$3<R<5\, \mathrm{kpc}$', color=color[6])
ax1l.plot(times[2:-2], -np.convolve((np.asarray(middle)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$7<R<9\, \mathrm{kpc}$', color=color[4])
ax1l.plot(times[2:-2], -np.convolve((np.asarray(middle3)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$9<R<13\, \mathrm{kpc}$', color='#ff7f0e')#color[2])
ax1l.plot(times[2:-2], -np.convolve((np.asarray(outer)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$13<R<17\, \mathrm{kpc}$', color=color[1])

ax1l.set_title('g8.26e11',fontsize=30)
ax1l.legend(ncol=2, fontsize=27)

# now we do g7.55e11
central = []
middle2 = []
middle3 = []
middle = []
outer = []
times = []

time_dict = pickle.load(open(paths.data / '7.55e11_time_dict.dat','rb'))

gas_profile_files = glob.glob('7.55e11.0????_cold_gas_profile.dat', root_dir=paths.data)
gas_profile_files.sort()

before = time_dict['00360']
after = time_dict['00520']
ax2l.plot([before,before],[.05,-1.55],color='darkgray')
ax2l.plot([after,after],[.05,-1.55],color='darkgray')

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(paths.data / f,'rb'))
    # in order to circumvent singularities when enrichment crosses [Fe/H] = 0, we subtract 1 from all values
    # we are anyways only interested in relative deviations.
    cen = np.where((0 < data['bins']) & (data['bins'] < 2))
    mid2 = np.where((3 < data['bins']) & (data['bins'] < 5))
    mid = np.where((7 < data['bins']) & (data['bins'] < 9))
    mid3 = np.where((9 < data['bins']) & (data['bins'] < 13))
    out = np.where((13 < data['bins']) & (data['bins'] < 17))
    central.append(np.mean(data['feh'][cen])-1)
    middle.append(np.mean(data['feh'][mid])-1)
    middle2.append(np.mean(data['feh'][mid2])-1)
    middle3.append(np.mean(data['feh'][mid3])-1)
    outer.append(np.mean(data['feh'][out])-1)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

ax2l.plot(times[2:-2], -np.convolve((np.asarray(middle2)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid') , label='$3<R<5\, \mathrm{kpc}$', color=color[6])
ax2l.plot(times[2:-2], -np.convolve((np.asarray(middle)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$7<R<9\, \mathrm{kpc}$', color=color[4])
ax2l.plot(times[2:-2], -np.convolve((np.asarray(middle3)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$9<R<13\, \mathrm{kpc}$', color='#ff7f0e')#color[2])
ax2l.plot(times[2:-2], -np.convolve((np.asarray(outer)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$13<R<17\, \mathrm{kpc}$', color=color[1])

ax2l.set_title('g7.55e11',fontsize=30)
ax2l.legend(ncol=2, fontsize=27)

# now we do g7.08e11
central = []
middle2 = []
middle3 = []
middle = []
outer = []
times = []

time_dict = pickle.load(open(paths.data / '7.08e11_time_dict.dat','rb'))

gas_profile_files = glob.glob('7.08e11.0????_cold_gas_profile.dat', root_dir=paths.data)
gas_profile_files.sort()

before = time_dict['00192']
after = time_dict['00356']
ax3l.plot([before,before],[.05,-1.55],color='darkgray')
ax3l.plot([after,after],[.05,-1.55],color='darkgray')

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(paths.data / f,'rb'))
    # in order to circumvent singularities when enrichment crosses [Fe/H] = 0, we subtract 1 from all values
    # we are anyways only interested in relative deviations.
    cen = np.where((0 < data['bins']) & (data['bins'] < 2))
    mid2 = np.where((3 < data['bins']) & (data['bins'] < 5))
    mid = np.where((7 < data['bins']) & (data['bins'] < 9))
    mid3 = np.where((9 < data['bins']) & (data['bins'] < 13))
    out = np.where((13 < data['bins']) & (data['bins'] < 17))
    central.append(np.mean(data['feh'][cen])-1)
    middle.append(np.mean(data['feh'][mid])-1)
    middle2.append(np.mean(data['feh'][mid2])-1)
    middle3.append(np.mean(data['feh'][mid3])-1)
    outer.append(np.mean(data['feh'][out])-1)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

ax3l.plot(times[2:-2], -np.convolve((np.asarray(middle2)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid') , label='$3<R<5\, \mathrm{kpc}$', color=color[6])
ax3l.plot(times[2:-2], -np.convolve((np.asarray(middle)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$7<R<9\, \mathrm{kpc}$', color=color[4])
ax3l.plot(times[2:-2], -np.convolve((np.asarray(middle3)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$9<R<13\, \mathrm{kpc}$', color='#ff7f0e')#color[2])
ax3l.plot(times[2:-2], -np.convolve((np.asarray(outer)-np.asarray(central))/(np.asarray(central)), np.ones(N)/N, mode='valid'), label='$13<R<17\, \mathrm{kpc}$', color=color[1])

ax3l.set_title('g7.08e11',fontsize=30)
ax3l.legend(ncol=2, fontsize=27)

plt.savefig(paths.figures / 'enrichment_evolution.pdf', bbox_inches='tight')