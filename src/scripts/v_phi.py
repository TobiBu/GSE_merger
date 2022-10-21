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
    #"font.family": "Helvetica"
})

data_main = pickle.load(open(paths.data / '2.79e12..00292_main_halo_cold_gas.dat','rb'))
p = plt.hist(data_main['v_phi_gas'],bins=50, histtype='step', label='$\mathrm{before\, merger}$', density=True)
#print(np.mean(data_main['v_phi_gas']))
data_main2 = pickle.load(open(paths.data / '2.79e12..00480_main_halo_cold_gas.dat','rb'))
p = plt.hist(data_main2['v_phi_gas'],bins=50, histtype='stepfilled', label='$\mathrm{after\, merger}$', density=True)
#print(np.mean(data_main2['v_phi_gas']))
plt.legend()
plt.xlabel('$v_\\phi\, [\mathrm{km/s}]$')
plt.ylabel('$\mathrm{d} f/\mathrm{d} v_\\phi$')
plt.savefig(paths.figures / '2.79e12_v_phi_gas.pdf', bbox_inches='tight')