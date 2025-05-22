from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='ortho',lon_0=0,lat_0=90,resolution='c')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
map.drawcountries()
parallels = np.arange(-90,90,15)
map.drawparallels(parallels, dashes=[1,0])
meridians = np.arange(-180,180,15)
map.drawmeridians(meridians, latmax=90, dashes=[1,0])

plt.show()
