import pandas as pd

birddata = pd.read_csv('bird_tracking.csv')

birddata.info()

birddata.head()

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == 'Eric'

x, y = birddata.longitude[ix], birddata.latitude[ix]

plt.figure(figsize = (7,7))

plt.plot(x, y, '.')


bird_names = pd.unique(birddata.bird_name)

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]    
    plt.plot(x, y, '.', label=bird_name)

plt.xlabel('longitude')
plt.ylabel('latitude')
plt.legend(loc = 'lower right')
plt.savefig('3traj.pdf') 

ix = birddata.bird_name == 'Eric'
speed = birddata.speed_2d[ix]
plt.hist(speed)
plt.hist(speed[:10])

np.isnan(speed)
np.isnan(speed).any()
np.sum(np.isnan(speed))

ix = birddata.bird_name == 'Eric'
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig('hist.pdf')


plt.figure(figsize = (8, 4))
ix = birddata.bird_name == 'Eric'
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), normed = True)
plt.xlabel('2D_Spped, (m/s)')
plt.ylabel('Frequency')
plt.savefig('hist.pdf')

birddata.speed_2d.plot(kind = 'hist', range = [0, 30])
plt.xlabel('2D_Speed');
plt.savefig('pd.hist.pdf')


import datetime

time_1 = datetime.datetime.today()
time_2 = datetime.datetime.today()
time_2 - time_1
print(time_2 - time_1)

date_str = birddata.date_time[0]
datetime.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')


timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
                      (birddata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
        
birddata['timestamp'] = pd.Series(timestamps, index = birddata.index)

        
    
times = birddata.timestamp[birddata.bird_name == 'Eric']
elapsed_time = [time - times[0] for time in times]   #???

elapsed_time[1000] / datetime.timedelta(days=1)

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel('observations')
plt.ylabel('elapsed_time (days)');
plt.savefig('timeplot.pdf')



data = birddata[birddata.bird_name == 'Eric']
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
next_day = 1
inds = []
daily_mean_speed = []
for i, t in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize = (8,6))
plt.plot(daily_mean_speed)
plt.xlabel('day')      
plt.ylabel('mean speed, (m/s)')  
plt.savefig('mean_speed.pdf')
        
times = birddata.timestamp[birddata.bird_name == 'Sanne']

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
plt.figure(figsize = (10,10))

ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, Linestyle = ':')
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label = bird_name)
plt.legend(loc = 'upper left')
plt.savefig('map.pdf')
    