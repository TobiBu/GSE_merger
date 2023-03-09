import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
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

data_main = pickle.load(open( paths.data / '2.79e12..00292_halo0_total_age_fe.dat','rb'))
data_main2 = pickle.load(open( paths.data / '2.79e12..00376_halo0_total_age_fe.dat','rb'))
data_main3 = pickle.load(open( paths.data / '2.79e12..01350_halo0_total_age_fe.dat','rb'))
data = pickle.load(open( paths.data / '2.79e12..00292_halo2_total_age_fe.dat','rb'))
data2 = pickle.load(open( paths.data / '2.79e12..00376_halo1_total_age_fe.dat','rb'))
data3 = pickle.load(open( paths.data / '2.79e12..00376_halo8_total_age_fe.dat','rb'))
data4 = pickle.load(open( paths.data / '2.79e12..01350_halo1_total_age_fe.dat','rb'))

fig = plt.figure(figsize=(36,6))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax3 = plt.subplot(gs[3])

ax.set_ylabel('$\mathrm{d} f/\mathrm{d[Fe/H]}$')
ax.set_xlabel('$\mathrm{[Fe/H]}$')
ax1.set_xlabel('$\mathrm{[Fe/H]}$')
ax2.set_xlabel('$\mathrm{[Fe/H]}$')
ax3.set_xlabel('$\mathrm{[Fe/H]}$')

ax.set_ylim(0,3.8)
ax1.set_ylim(0,3.8)
ax2.set_ylim(0,3.8)
ax3.set_ylim(0,3.8)

ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax3.set_yticklabels([])

# first merger
ax3.hist(data_main['feh'],bins=50, histtype='step', color='k', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax3.hist(data_main['feh_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax3.hist(data['feh'],bins=50, histtype='step', range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, stars}$')
ax3.hist(data['feh_gas'],bins=50, histtype='stepfilled', alpha=.5, range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, gas}$')

ax3.text(-1.75, 3.2, '$t=%.2f\,\mathrm{Gyr}$'%time_dict['00292'])
ax3.legend(ncol=4, loc=1, bbox_to_anchor=(.6,1.225))#, fontsize=24)

# second merger
ax2.hist(data_main2['feh'],bins=50, histtype='step', color='k', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax2.hist(data_main2['feh_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax2.hist(data2['feh'],bins=50, histtype='step', range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 1\, stars}$')
ax2.hist(data2['feh_gas'],bins=50, histtype='stepfilled', alpha=0.5,range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 1\, gas}$')

ax2.text(-1.75, 3.2, '$t=%.2f\,\mathrm{Gyr}$'%time_dict['00376']) # done merging by 3 Gyr

# third merger
ax1.hist(data_main2['feh'],bins=50, histtype='step', color='k', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax1.hist(data_main2['feh_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax1.hist(data3['feh'],bins=50, histtype='step', range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 2\, stars}$')
ax1.hist(data3['feh_gas'],bins=50, histtype='stepfilled', alpha=0.5, range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 2\, gas}$')

ax1.text(-1.75, 3.2, '$t=%.2f\,\mathrm{Gyr}$'%time_dict['00376']) # done merging by 3 Gyr

# fourth merger
ax.hist(data_main3['feh'],bins=50, histtype='step', color='k', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax.hist(data_main3['feh_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(-3.05,0.55), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax.hist(data4['feh'],bins=50, histtype='step', range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 2\, stars}$')
ax.hist(data4['feh_gas'],bins=50, histtype='stepfilled', alpha=0.5, range=(-3.05,0.55), density=True, label='$\mathrm{merger\, galaxy\, 2\, gas}$')

ax.text(-1.75, 3.2, '$t=%.2f\,\mathrm{Gyr}$'%time_dict['01350']) # done merging by 3 Gyr

plt.savefig(paths.figures / '2.79e12_mdf_gas.pdf', bbox_inches='tight')