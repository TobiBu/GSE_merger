import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pickle, paths

fig = plt.figure(figsize=(30,5))
gs = gridspec.GridSpec(1, 4, width_ratios=[1,1,1,1], height_ratios=[1])
gs.update(hspace=0.0, wspace=0.0)
ax = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2])
ax3 = plt.subplot(gs[3])
ax.set_ylabel("$\mathrm{[O/Fe]}$")
ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax3.set_yticklabels([])
ax.set_xlabel("$\mathrm{[Fe/H]}$")
ax1.set_xlabel("$\mathrm{[Fe/H]}$")
ax2.set_xlabel("$\mathrm{[Fe/H]}$")
ax3.set_xlabel("$\mathrm{[Fe/H]}$")

time_dict = pickle.load(open(paths.data / '2.79e12_time_dict.dat','rb'))

data = pickle.load(open(paths.data / '2.79e12_age_fe.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax1.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax2.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')
ax3.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto', cmap='Greys')

data = pickle.load(open(paths.data / '2.79e12.01350_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Blues')
ax.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['01350'])

data = pickle.load(open(paths.data / '2.79e12.00376_age_fe_halo8_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax1.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Greens')
ax1.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])


data = pickle.load(open(paths.data / '2.79e12.00376_age_fe_halo1_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax2.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Purples')
ax2.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00376'])


data = pickle.load(open(paths.data / '2.79e12.00292_age_fe_halo2_stars.dat','rb'))
hist, xe, ye = np.histogram2d(data['feh'],data['ofe'],range=((-3,0.75),(-0,0.6)),bins=200)
ax3.imshow(np.log(hist).T, origin='lower', extent=((-3,0.75,-0,0.6)), aspect='auto',cmap='Oranges')
ax3.set_title("$\mathrm{merger\, at\, }t=%.2f\, \mathrm{Gyr}$"%time_dict['00292'])

plt.savefig(paths.figures / '2.79e12_feh_ofe_grid.pdf", bbox_inches='tight')