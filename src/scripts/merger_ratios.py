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

fig = plt.figure(figsize=(45,10))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
axl = plt.subplot(gs[0])
ax1l = plt.subplot(gs[1])
ax2l = plt.subplot(gs[2])
ax3l = plt.subplot(gs[3])
axl.set_ylabel("$M_{\mathrm{gas}}\, [M_\odot]$")
ax1l.set_yticklabels([])
ax2l.set_yticklabels([])
ax3l.set_yticklabels([])
axl.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax1l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax2l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax3l.set_xlabel("$\mathrm{time\ [Gyr]}$")

axl.set_ylim(1e7,4e11)
axl.set_xlim(0,14)
ax1l.set_xlim(0,14)
ax1l.set_ylim(1e7,4e11)
ax2l.set_xlim(0,14)
ax2l.set_ylim(1e7,4e11)
ax3l.set_xlim(0,14)
ax3l.set_ylim(1e7,4e11)

#let's do g2.79e12

data = pickle.load(open(paths.data / '2.79e12_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))

axl.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
axl.text(7,5e10,'g2.79e12',fontsize=30)
axl.set_yscale('log')

ax = axl.twinx()
ax.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax.spines['right'].set_color('darkorange')
ax.yaxis.label.set_color('darkorange')
ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-2,75)

# now g7.55e11
data = pickle.load(open(paths.data / '7.55e11_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))

axl.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
axl.text(7,5e10,'g7.55e11',fontsize=30)
axl.set_yscale('log')

ax = axl.twinx()
ax.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax.spines['right'].set_color('darkorange')
ax.yaxis.label.set_color('darkorange')
ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-2,75)


# now we do g7.08e11
data = pickle.load(open(paths.data / '7.08e11_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))

axl.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
axl.text(7,5e10,'g7.08e11',fontsize=30)
axl.set_yscale('log')

ax = axl.twinx()
ax.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax.spines['right'].set_color('darkorange')
ax.yaxis.label.set_color('darkorange')
ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-2,75)

# now we do g8.26e11
data = pickle.load(open(paths.data / '2.79e12_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))

axl.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
axl.text(7,5e10,'g2.79e12',fontsize=30)
axl.set_yscale('log')

ax = axl.twinx()
ax.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax.spines['right'].set_color('darkorange')
ax.yaxis.label.set_color('darkorange')
ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-2,75)

#plt.spines['right'].set_color('darkorange')

plt.savefig(paths.figures / 'merger_ratios.pdf', bbox_inches='tight')