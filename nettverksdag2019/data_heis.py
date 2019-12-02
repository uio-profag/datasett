from pylab import *

# Leser av fila
data = loadtxt('Datafiler/heistur.csv', delimiter = ',', skiprows = 1)
t = data[:,0]
h = data[:,2]

# Derivasjonsvariabler
n = len(t)
v = zeros(n)
a = zeros(n)
v[0] = 0

# Derivasjonsløkke
for i in range(0, n-1):
    v[i+1] = (h[i+1] - h[i])/(t[i+1] - t[i])
    
plot(t, v, color = 'red')
title('Heistur')
xlabel('Tid (s)')
ylabel('Hastighet (m/s)')
grid()
show()