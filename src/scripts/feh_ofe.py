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
    "text.usetex": False,
    "font.family": "Helvetica"
})

fig = plt.figure(figsize=(30,10))
gs = gridspec.GridSpec(2, 4, width_ratios=[1,1,1,1], height_ratios=[1,1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax3 = plt.subplot(gs[3])

ax4 = plt.subplot(gs[4])
ax5 = plt.subplot(gs[5])
ax6 = plt.subplot(gs[6])
ax7 = plt.subplot(gs[7])

ax.set_ylabel("$\mathrm{[O/Fe]}$")
ax4.set_ylabel("$\mathrm{[O/Fe]}$")

ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax3.set_yticklabels([])

ax.set_xticklabels([])
ax1.set_xticklabels([])
ax2.set_xticklabels([])
ax3.set_xticklabels([])


ax5.set_yticklabels([])
ax6.set_yticklabels([])
ax7.set_yticklabels([])

ax4.set_xlabel("$\mathrm{[Fe/H]}$")
ax5.set_xlabel("$\mathrm{[Fe/H]}$")
ax6.set_xlabel("$\mathrm{[Fe/H]}$")
ax7.set_xlabel("$\mathrm{[Fe/H]}$")

time_dict = pickle.load(open( paths.data / '2.79e12_time_dict.dat','rb'))

data = pickle.load(open( paths.data / '2.79e12_age_fe.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax1.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax2.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax3.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')

ax4.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax5.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax6.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax7.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')

data = pickle.load(open( paths.data / '2.79e12.01350_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Blues')
ax.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['01350'])

data = pickle.load(open( paths.data / '2.79e12.01350_alpha_fe_halo1_gas.dat','rb'))
xe = data['xbins']
ye = data['ybins']
mass = data['mass']

x = (xe[1:]+xe[:-1])/2.
y = (ye[1:]+ye[:-1])/2.

cs = ax4.contour(x,y,np.log10(mass.T), levels=[3,4,5.25,6.25,6.75], cmap='Blues', linewidths=2.5, extent=((-3,0.75,-0,0.6)))
ax4.set_ylim(-0,0.6)
ax4.set_xlim(-3,0.75)

data = pickle.load(open( paths.data / '2.79e12.00376_age_fe_halo8_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax1.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Greens')
ax1.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])

data = pickle.load(open( paths.data / '2.79e12.00376_alpha_fe_halo8_gas.dat','rb'))
xe = data['xbins']
ye = data['ybins']
mass = data['mass']

x = (xe[1:]+xe[:-1])/2.
y = (ye[1:]+ye[:-1])/2.

cs = ax5.contour(x,y,np.log10(mass.T), levels=[3,4,5.25,6.25,6.75], cmap='Greens', linewidths=2.5, extent=((-3,0.75,-0,0.6)))
ax5.set_ylim(-0,0.6)
ax5.set_xlim(-3,0.75)

data = pickle.load(open( paths.data / '2.79e12.00376_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax2.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Purples')
ax2.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])

data = pickle.load(open( paths.data / '2.79e12.00376_alpha_fe_halo1_gas.dat','rb'))
xe = data['xbins']
ye = data['ybins']
mass = data['mass']

x = (xe[1:]+xe[:-1])/2.
y = (ye[1:]+ye[:-1])/2.

cs = ax6.contour(x,y,np.log10(mass.T), levels=[3,4,5.25,6.25,6.75], cmap='Purples', linewidths=2.5, extent=((-3,0.75,-0,0.6)))
ax6.set_ylim(-0,0.6)
ax6.set_xlim(-3,0.75)

data = pickle.load(open( paths.data / '2.79e12.00292_age_fe_halo2_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax3.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Oranges')
ax3.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00292'])

data = pickle.load(open( paths.data / '2.79e12.00292_alpha_fe_halo2_gas.dat','rb'))
xe = data['xbins']
ye = data['ybins']
mass = data['mass']

x = (xe[1:]+xe[:-1])/2.
y = (ye[1:]+ye[:-1])/2.

cs = ax7.contour(x,y,np.log10(mass.T), levels=[3,4,5.25,6.25,6.75], cmap='Oranges', linewidths=2.5, extent=((-3,0.75,-0,0.6)))
ax7.set_ylim(-0,0.6)
ax7.set_xlim(-3,0.75)

ax.text(-.05,.5, "$\mathrm{stars}$")
ax1.text(-.05,.5, "$\mathrm{stars}$")
ax2.text(-.05,.5, "$\mathrm{stars}$")
ax3.text(-.05,.5, "$\mathrm{stars}$")

ax4.text(-.05,.5, "$\mathrm{gas}$")
ax5.text(-.05,.5, "$\mathrm{gas}$")
ax6.text(-.05,.5, "$\mathrm{gas}$")
ax7.text(-.05,.5, "$\mathrm{gas}$")


plt.savefig(paths.figures / '2.79e12_feh_ofe_grid.pdf', bbox_inches='tight')