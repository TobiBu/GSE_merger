import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pickle, paths

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

time_dict = pickle.load(open( paths.data / '2.79e12_time_dict.dat','rb'))

fig = plt.figure(figsize=(30, 10))
gs = gridspec.GridSpec(1, 2, width_ratios=[1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])

#first merger
snaps = ['.00360','.00350','.00340','.00330','.00292']

from matplotlib.pyplot import cm
color = cm.seismic_r(np.linspace(0,1,len(snaps)+1))

data = pickle.load(open( paths.data / '2.79e12.00376_cold_gas_profile.dat','rb'))
ax.plot(data['bins'],data['feh'],label='$%.2f\,\mathrm{Gyr}$'%time_dict['00376'], color='dimgrey')

i = 0
for snap in snaps:
    file = '2.79e12' + snap + '_cold_gas_profile.dat'
    data = pickle.load(open(paths.data / file,'rb'))
    ax.plot(data['bins'],data['feh'],label='$%.2f\,\mathrm{Gyr}$'%time_dict[snap[1:]], color=color[i])
    if i == 2:
        i+=1
    i+=1

data = pickle.load(open( paths.data / '2.79e12.00292_cold_gas_profile.dat','rb'))
ax.plot(data['bins'],data['feh'], color='darkblue')

ax.set_ylim(-1.9,-0.2)
ax.set_ylabel("$\mathrm{[Fe/H]}$")
ax.set_xlabel("$\mathrm{radius\ [kpc]}$")
ax.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00292'])
ax.legend()

# now second merger
snaps = ['.00470','.00430','.00400','.00390','.00376']

i = 0

data = pickle.load(open( paths.data / '2.79e12.00560_cold_gas_profile.dat','rb'))
ax1.plot(data['bins'],data['feh'],label='$%.2f\,\mathrm{Gyr}$'%time_dict['00560'], color='dimgrey')

i = 0
for snap in snaps:
    file = '2.79e12' + snap + '_cold_gas_profile.dat'
    data = pickle.load(open(paths.data / file,'rb'))
    ax1.plot(data['bins'],data['feh'],label='$%.2f\,\mathrm{Gyr}$'%time_dict[snap[1:]], color=color[i])
    if i == 2:
        i+=1
    i+=1

data = pickle.load(open( paths.data / '2.79e12.00376_cold_gas_profile.dat','rb'))
ax1.plot(data['bins'],data['feh'], color='darkblue')

ax1.set_ylim(-1.9,-0.2)
#ax1.ylabel("$\mathrm{[Fe/H]}$")
ax1.set_yticklabels([])
ax1.set_xlabel("$\mathrm{radius\ [kpc]}$")
ax1.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])
ax1.legend()

fig.savefig(paths.figures / "feh_gradient.pdf", bbox_inches='tight')