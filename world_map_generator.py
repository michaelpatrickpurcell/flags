from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# map = Basemap(projection='ortho',lat_0=-35, lon_0=149, resolution='c', round=True)
map = Basemap(projection='robin',lat_0=0, lon_0=0, resolution='c', round=True)
# map = Basemap(projection='merc',lat_0=0, lon_0=90, resolution='c',llcrnrlat=-57.5,urcrnrlat=80, llcrnrlon=-170,urcrnrlon=192)

circle = map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='olive',lake_color='lightblue')
map.drawcoastlines()
map.drawcountries()
parallels = np.arange(-90,90,15)
map.drawparallels(parallels, dashes=[1,0], latmax=0, linewidth=0.25, zorder=5)
meridians = np.arange(-180,180,15)
# meridians = np.arange(-180,180,20)
map.drawmeridians(meridians, latmax=90, dashes=[1,0], linewidth=0.25, zorder=5)
circle.set_clip_on(False)

# map.bluemarble()
data = map.readshapefile('./Data/ATA/gadm41_ATA_0', 'focus_country')
country = data[4]
country.set_facecolors('silver')

lats = [-90]
lons = [0]
x,y = map(lons, lats)
map.scatter(x,y, s=150, marker='.', color='red', zorder=10)

plt.savefig('Images/Maps/aq_map.png', dpi=300, transparent=True, bbox_inches='tight')
# plt.savefig('Images/test3.png', dpi=300, bbox_inches='tight')

plt.show()