import numpy as np
import matplotlib.pyplot as plt
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

simname = '2.79e12' #'7.55e11'

import sys
sys.setrecursionlimit(50000)

data = pickle.load(open(paths.data / '2.79e12_merger_tree.dat','rb'))
merger_tree = data['merger_tree']

star_ratio = []
gas_ratio = []
mass_ratio = []

time = merger_tree['prog', 'time']
mass = merger_tree['prog', 'mass']
star_mass = merger_tree['prog', 'M_star']
gas_mass = merger_tree['prog', 'M_gas']

for node in list(merger_tree['prog']):
    prog_mass = node['mass']
    prog_star = node['M_star']
    prog_gas = node['M_gas']
    ratio = [x['mass']/prog_mass for x in list(node.ancestors)]
    try:
        mass_ratio.append(np.max(ratio[ratio!=0]))
    except:
        pass
    ratio = [x['M_star']/prog_star for x in list(node.ancestors)]
    try:
        star_ratio.append(np.max(ratio[ratio!=0]))
    except:
        pass
    ratio = [x['M_gas']/prog_gas for x in list(node.ancestors)]
    try:
        gas_ratio.append(np.max(ratio[ratio!=0]))
    except:
        pass

# gas mass ratio
plt.plot(time/1000.,gas_mass)
plt.xlabel("$\mathrm{time\, [Gyr]}$")
plt.ylabel("$M_{\mathrm{gas}}\, [M_\odot]$")
plt.yscale('log')

ax = plt.twinx()
ax.plot(time[:-5]/1000.,gas_ratio,c='orange')
ax.set_ylabel("$\mathrm{merger\, ratio}$")

plt.savefig(paths.figures / simname+'merger_ratio_gas.pdf', bbox_inches='tight')

plt.clf()

# stellar mass ratio
plt.plot(time/1000.,star_mass)
plt.xlabel("$\mathrm{time\, [Gyr]}$")
plt.ylabel("$M_{\mathrm{star}}\, [M_\odot]$")
plt.yscale('log')

ax = plt.twinx()
ax.plot(time[:-5]/1000.,star_ratio, c='orange')
ax.set_ylabel("$\mathrm{merger\, ratio}$")

plt.savefig(paths.figures / simname+'merger_ratio_stars.pdf', bbox_inches='tight')

plt.clf()

# total mass ratio
plt.plot(time/1000.,mass)
plt.xlabel("$\mathrm{time\, [Gyr]}$")
plt.ylabel("$M_{\mathrm{tot}}\, [M_\odot]$")
plt.yscale('log')

ax = plt.twinx()
ax.plot(time[:-5]/1000.,mass_ratio, c='orange')
ax.set_ylabel("$\mathrm{merger\, ratio}$")

plt.savefig(paths.figures / simname+'merger_ratio_tot_mass.pdf', bbox_inches='tight')

