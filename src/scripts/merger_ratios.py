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
axl.set_ylabel("$M_{\mathrm{gas}}\, [M_\odot]$")
axl.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax1l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax2l.set_xlabel("$\mathrm{time\ [Gyr]}$")
ax3l.set_xlabel("$\mathrm{time\ [Gyr]}$")

axl.set_ylim(1e7,4e11)
axl.set_xlim(0,13.9)
ax1l.set_xlim(0,13.9)
ax1l.set_ylim(1e7,4e11)
ax2l.set_xlim(0,13.9)
ax2l.set_ylim(1e7,4e11)
ax3l.set_xlim(0,13.9)
ax3l.set_ylim(1e7,4e11)

#let's do g2.79e12

data = pickle.load(open(paths.data / '2.79e12_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))[::-1]

axl.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
axl.text(7,5e10,'g2.79e12',fontsize=30)
axl.set_yscale('log')
axl.spines['left'].set_color('#1f77b4')
axl.yaxis.label.set_color('#1f77b4')
axl.tick_params(axis='y', colors='#1f77b4')

ax = axl.twinx()
ax.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax.spines['left'].set_visible(False)
#ax.yaxis.label.set_color('darkorange')
ax.tick_params(axis='y', colors='orange')
ax.set_yticklabels([])
ax.set_ylim(-.02,.35)

# now g8.26e11
data = pickle.load(open(paths.data / '8.26e11_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))[::-1]

ax1l.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
ax1l.text(7,5e10,'g8.26e11',fontsize=30)
ax1l.tick_params(axis='y', colors='#1f77b4')
ax1l.set_yscale('log')
ax1l.set_yticklabels([])
ax1 = ax1l.twinx()
ax1.spines['left'].set_visible(False)
ax1.plot(time[:-3],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

#ax1.spines['right'].set_color('darkorange')
#ax1.yaxis.label.set_color('darkorange')
ax1.tick_params(axis='y', colors='orange')
ax1.set_yticklabels([])
ax1.set_ylim(-.02,.35)


# now we do g7.55e11
data = pickle.load(open(paths.data / '7.55e11_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))[::-1]

ax2l.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
ax2l.text(7,5e10,'g7.55e11',fontsize=30)
ax2l.tick_params(axis='y', colors='#1f77b4')
ax2l.set_yscale('log')
ax2l.set_yticklabels([])
ax2 = ax2l.twinx()
ax2.spines['left'].set_visible(False)
ax2.plot(time[:-2],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

#ax2.spines['right'].set_color('darkorange')
#ax2.yaxis.label.set_color('darkorange')
ax2.tick_params(axis='y', colors='orange')
ax2.set_yticklabels([])
ax2.set_ylim(-.02,.35)

# now we do g7.08e11
data = pickle.load(open(paths.data / '7.08e11_merger_tree_data.dat','rb'))
time = np.linspace(0,13.8, len(data['gas_mass']))[::-1]

ax3l.plot(time, data['gas_mass'], label='$\mathrm{gas/, mass}$' )
ax3l.text(7,5e10,'g7.08e11',fontsize=30)
ax3l.tick_params(axis='y', colors='#1f77b4')
ax3l.set_yscale('log')
ax3l.set_yticklabels([])
ax3 = ax3l.twinx()
ax3.spines['left'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.plot(time[:-5],data['gas_ratio'],c='darkorange', label='$\mathrm{merger\ ratio\ gas}$')

ax3l.spines['right'].set_color('darkorange')
ax3.yaxis.label.set_color('darkorange')
ax3.tick_params(axis='y', colors='orange')
ax3.set_ylim(-.02,.35)
ax3.set_ylabel("$\mathrm{merger\, ratio}$")

plt.savefig(paths.figures / 'merger_ratios.pdf', bbox_inches='tight')