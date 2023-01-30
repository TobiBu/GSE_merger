import matplotlib.pylab as plt
import pickle, paths
import matplotlib.gridspec as gridspec

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
axl.set_ylabel("$\Delta\rho\mathrm{[M_\odot/kpc^2]}$")
ax1l.set_yticklabels([])
ax2l.set_yticklabels([])
ax3l.set_yticklabels([])
axl.set_xlabel("$\mathrm{radius\ [kpc]}$")
ax1l.set_xlabel("$\mathrm{radius\ [kpc]}$")
ax2l.set_xlabel("$\mathrm{radius\ [kpc]}$")
ax3l.set_xlabel("$\mathrm{radius\ [kpc]}$")

axl.set_ylim(-.105,0.0)
#axl.set_xlim(0,13.9)
#ax1l.set_xlim(0,13.9)
ax1l.set_ylim(-.105,0.0)
#ax2l.set_xlim(0,13.9)
ax2l.set_ylim(-.105,0.0)
#ax3l.set_xlim(0,13.9)
ax3l.set_ylim(-.105,0.0)

snaps = ['2.79e12.00292_gas_profile.dat','2.79e12.00480_gas_profile.dat']
labels = ['$\mathrm{before\, merger}$', '$\mathrm{after\, merger}$']

for snap, label in zip(snaps, labels):

    data = pickle.load(open(paths.data / snap,'rb'))
    plt.plot(data['bins'],data['density'],label=label)

#plt.ylim(-5,1)
plt.yscale('log')
plt.ylabel("$\\rho\mathrm{[M_\odot/kpc^2]}$")
plt.xlabel("$\mathrm{radius\ [kpc]}$")
plt.legend()
plt.savefig(paths.figures / "2.79e12_gas_profile_2d.pdf", bbox_inches='tight')