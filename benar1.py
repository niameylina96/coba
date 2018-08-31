from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

peta = Basemap(projection='merc', lat_0=0, lon_0=125,
	       resolution='l', area_thresh=0.1,
	       llcrnrlon=90, llcrnrlat=-15,
	       urcrnrlon=155, urcrnrlat=15)

plt.figure()
peta.drawcoastlines()
peta.drawcountries()
peta.bluemarble()

lon = [107.668710,107.668663,107.668610,107.574970,107.575090,]
lat = [-6.972280,-6.972270,-6.972270,-6.943540,-6.943390]
x, y = peta(lon,lat)
peta.plot(x,y,'ro',markersize=5)

plt.show()
