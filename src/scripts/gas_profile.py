import matplotlib.pylab as plt
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