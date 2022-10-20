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

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

slopes = []
times = []
N = 5  # window size for running average of gradient

fig = plt.figure(figsize=(45,10))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
axl = plt.subplot(gs[0])
ax1l = plt.subplot(gs[1])
ax2l = plt.subplot(gs[2])
ax3l = plt.subplot(gs[3])
axl.set_ylabel("$\Delta\mathrm{[Fe/H]\ dex/kpc}$")
ax1l.set_yticklabels([])
ax2l.set_yticklabels([])
ax3l.set_yticklabels([])
axl.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax1l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax2l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax3l.set_xlabel("$\mathrm{time\ [Gyr]}$")

axl.set_ylim(-.105,0.0)
axl.set_xlim(0,14)
ax1l.xlim(0,14)
ax1l.ylim(-.105,0.0)
ax2l.xlim(0,14)
ax2l.ylim(-.105,0.0)
ax3l.xlim(0,14)
ax3l.ylim(-.105,0.0)

#let's do g2.79e12

# the central and most outer parts of the profile deviate from a linear relation, so we cut them
l = 5
r = -5

time_dict = pickle.load(open(paths.data / '2.79e12_time_dict.dat','rb'))

gas_profile_files = glob.glob(paths.data / '2.79e12.0????_cold_gas_profile.dat')
gas_profile_files.sort()

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(f,'rb'))
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['bins'][l:r],data['feh'][l:r])
    slopes.append(slope)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

axl.plot(times, np.convolve(slopes, np.ones(N)/N, mode='same') )

ax = axl.twinx()
data = pickle.load(open(paths.data / '2.79e12_rhalf.dat','rb'))
ax.plot(data['time'],data['rhalf_cold'],c='darkorange')
#ax.set_ylabel("$R_{\mathrm{half}}\ \mathrm{[kpc]}$")

ax.spines['right'].set_color('darkorange')
ax.yaxis.label.set_color('darkorange')
#ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-2,75)

# now g7.55e11
slopes = []
times = []

l = 0
r = -2

time_dict = pickle.load(open(paths.data / '7.55e11_time_dict.dat','rb'))

gas_profile_files = glob.glob(paths.data / '7.55e11.0????_cold_gas_profile.dat')
gas_profile_files.sort()

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(f,'rb'))
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['bins'][l:r],data['feh'][l:r])
    slopes.append(slope)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

ax1l.plot(times, np.convolve(slopes, np.ones(N)/N, mode='same'))

ax1 = ax1l.twinx()
data = pickle.load(open(paths.data / '7.55e11_rhalf.dat','rb'))
ax1.plot(data['time'],data['rhalf_cold'],c='darkorange')

ax1.spines['right'].set_color('darkorange')
ax1.yaxis.label.set_color('darkorange')
#ax.tick_params(axis='y', colors='darkorange')
ax1.set_yticklabels([])
ax1.set_ylim(-2,75)


# now we do g7.08e11
slopes = []
times = []

l = 2
r = -5

time_dict = pickle.load(open(paths.data / '7.08e11_time_dict.dat','rb'))

gas_profile_files = glob.glob(paths.data / '7.08e11.0????_cold_gas_profile.dat')
gas_profile_files.sort()

for i, f in enumerate(gas_profile_files[::-1]):
    data = pickle.load(open(f,'rb'))
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['bins'][l:r],data['feh'][l:r])
    slopes.append(slope)
    times.append(time_dict[f.split('_')[0].split('.')[-1]])

ax2l.plot(times, np.convolve(slopes, np.ones(N)/N, mode='same'))

ax2 = ax2l.twinx()
data = pickle.load(open(paths.data / 'data/7.08e11_rhalf.dat','rb'))
ax2.plot(data['time'],data['rhalf_cold'],c='darkorange')
#ax2.set_ylabel("$R_{\mathrm{half}}\ \mathrm{[kpc]}$")

ax2.spines['right'].set_color('darkorange')
ax2.yaxis.label.set_color('darkorange')
#ax2.tick_params(axis='y', colors='darkorange')
ax2.set_yticklabels([])
ax2.set_ylim(-2,75)


# now we do g8.26e11
ax3 = ax3l.twinx()
ax3.set_ylabel("$R_{\mathrm{half}}\ \mathrm{[kpc]}$")
ax3.spines['right'].set_color('darkorange')
ax3.yaxis.label.set_color('darkorange')
ax3.tick_params(axis='y', colors='darkorange')
ax3.set_yticklabels([])
ax3.set_ylim(-2,75)


plt.savefig(paths.figures / 'half_mass_radius_metal_gradient.pdf', bbox_inches='tight')