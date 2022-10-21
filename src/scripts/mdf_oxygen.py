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

plt.rcParams.update({
    "text.usetex": True,
    #"font.family": "Helvetica"
})

time_dict = pickle.load(open( paths.data / '2.79e12_time_dict.dat','rb'))

data_main = pickle.load(open( paths.data / '2.79e12..00292_halo0_total_age_fe.dat','rb'))
data_main2 = pickle.load(open( paths.data / '2.79e12..00376_halo0_total_age_fe.dat','rb'))
data = pickle.load(open( paths.data / '2.79e12..00292_halo2_total_age_fe.dat','rb'))
data2 = pickle.load(open( paths.data / '2.79e12..00376_halo1_total_age_fe.dat','rb'))
data3 = pickle.load(open( paths.data / '2.79e12..00376_halo8_total_age_fe.dat','rb'))

fig = plt.figure(figsize=(45, 10))
gs = gridspec.GridSpec(1, 3, width_ratios=[1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])

ax1.set_yticklabels([])
ax2.set_yticklabels([])

# first merger
ax.hist(data_main['ofe'],bins=50, histtype='step', color='k', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax.hist(data_main['ofe_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax.hist(data['ofe'],bins=50, histtype='step', range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, stars}$')
ax.hist(data['ofe_gas'],bins=50, histtype='stepfilled', alpha=.5, range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, gas}$')

ax.legend(loc=2, title='$t=%.2f\,\mathrm{Gyr}$'%time_dict['00292'])
ax.set_xlabel('$\mathrm{[O/Fe]}$')
ax.set_ylabel('$\mathrm{d} f/\mathrm{d[O/Fe]}$')
ax.set_ylim(0,15.8)


# second merger
ax1.hist(data_main2['ofe'],bins=50, histtype='step', color='k', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax1.hist(data_main2['ofe_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax1.hist(data2['ofe'],bins=50, histtype='step', range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, 1\, stars}$')
ax1.hist(data2['ofe_gas'],bins=50, histtype='stepfilled', alpha=0.5,range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, 1\, gas}$')

ax1.legend(loc=2, title='$t=%.2f\,\mathrm{Gyr}$'%time_dict['00376']) # done merging by 3 Gyr
ax1.set_xlabel('$\mathrm{[Fe/H]}$')
ax1.set_ylim(0,15.8)


ax2.hist(data_main2['ofe'],bins=50, histtype='step', color='k', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, stars}$')
ax2.hist(data_main2['ofe_gas'],bins=50, histtype='stepfilled', color='darkgray', range=(.10,0.6), density=True, label='$\mathrm{main\, galaxy\, gas}$')
ax2.hist(data3['ofe'],bins=50, histtype='step', range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, 2\, stars}$')
ax2.hist(data3['ofe_gas'],bins=50, histtype='stepfilled', alpha=0.5, range=(.10,0.6), density=True, label='$\mathrm{merger\, galaxy\, 2\, gas}$')

ax2.legend(loc=2, title='$t=%.2f\,\mathrm{Gyr}$'%time_dict['00376']) # done merging by 3 Gyr
ax2.set_xlabel('$\mathrm{[Fe/H]}$')
ax2.set_ylim(0,15.8)

plt.savefig(paths.figures / '2.79e12_mdf_oxygen_gas.pdf', bbox_inches='tight')