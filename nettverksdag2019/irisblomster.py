from pylab import *

data = loadtxt('Iris.csv',delimiter=',',
               skiprows = 1, usecols=(0,1,2,3,4))

sepal_length = data[:,1]
sepal_width = data[:,2]
petal_length = data[:,3]

hist(sepal_length,edgecolor='black')
show()
scatter(sepal_length, petal_length)
show()
