from pylab import *

fil = loadtxt('heistur.csv',delimiter=',',
              skiprows=1)

t = fil[:,0]
s = fil[:,2]
v = []

for i in range(len(t)-1):
    fart = (s[i+1] - s[i])/(t[i+1] - t[i])
    v.append(fart)
    
figure(figsize=(10,10))
plot(t[:-1],v,marker='o',color='hotpink')
xlabel('Tid (s)')
ylabel('Hastighet (m/s)')
show()
    
    
    
    
    
    
    
    
    
    