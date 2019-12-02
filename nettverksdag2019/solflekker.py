from pylab import *

fil = loadtxt('solflekker.txt')

maaned = fil[:,0]
solflekker = fil[:,1]

snitt = mean(solflekker)
avvik = std(solflekker)

print(snitt, avvik)

