from pylab import *

fil = loadtxt('Iris.csv', delimiter=',',
              skiprows = 1, usecols = (0,1,2,3,4))

begerlengde = fil[:,1]
begerbredde = fil[:,2]
kronlengde = fil[:,3]
kronbredde = fil[:,4]

hist(begerbredde,edgecolor='black',bins=20)
