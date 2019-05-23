import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

cities=list(np.arange(0,81,1))
cities.remove(5)
np.random.shuffle(cities)
cities=[5]+cities+[5]

x_coordinates,y_coordinates=coordinates[:,0],coordinates[:,1]
x_coordinates_,y_coordinates_=list(y_coordinates[cities]),list(x_coordinates[cities])

map=plt.imread('map.png')
plt.imshow(map, extent=[26,45,35.5,42.5])
plt.axes().set_aspect(1.3,'datalim')
plt.plot(x_coordinates_,y_coordinates_,linewidth=0.6)

total_distance=int(np.sum(distances[cities[1:],cities[:-1]]))
plt.text(27.5,34.7,'The total distance covered is %a km' %total_distance)
plt.savefig('image1',dpi=300)