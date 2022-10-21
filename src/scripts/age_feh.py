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

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

fig = plt.figure(figsize=(30,5))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax3 = plt.subplot(gs[3])
ax.set_ylabel("$\mathrm{[Fe/H]}$")
ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax3.set_yticklabels([])
ax.set_xlabel("$\mathrm{age\ [Gyr]}$")
ax1.set_xlabel("$\mathrm{age\ [Gyr]}$")
ax2.set_xlabel("$\mathrm{age\ [Gyr]}$")
ax3.set_xlabel("$\mathrm{age\ [Gyr]}$")

time_dict = pickle.load(open(paths.data / '2.79e12_time_dict.dat','rb'))

data = pickle.load(open(paths.data / '2.79e12_age_fe.dat','rb'))
hist, xe, ye = np.histogram2d(data['age'],data['feh'],range=((0,14),(-3.5,0.75)),bins=250)
ax.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto', cmap='Greys')
ax1.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto', cmap='Greys')
ax2.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto', cmap='Greys')
ax3.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto', cmap='Greys')

data = pickle.load(open(paths.data / '2.79e12.01350_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['age'],data['feh'],range=((0,14),(-3.5,0.75)),bins=150)
ax.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto',cmap='Blues')
ax.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['01350'])

data = pickle.load(open(paths.data / '2.79e12.00376_age_fe_halo8_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['age'],data['feh'],range=((0,14),(-3.5,0.75)),bins=150)
ax1.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto',cmap='Greens')
ax1.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])


data = pickle.load(open(paths.data / '2.79e12.00376_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['age'],data['feh'],range=((0,14),(-3.5,0.75)),bins=150)
ax2.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto',cmap='Purples')
ax2.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])


data = pickle.load(open(paths.data / '2.79e12.00292_age_fe_halo2_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['age'],data['feh'],range=((0,14),(-3.5,0.75)),bins=150)
ax3.imshow(np.log(hist).T, origin='lower', extent=((0,14,-3,0.75)), aspect='auto',cmap='Oranges')
ax3.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00292'])

plt.savefig(paths.figures / "2.79e12_age_metallicity_grid.pdf", bbox_inches='tight')