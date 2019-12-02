from pylab import *

N = 10000
seksere = 0

for i in range(N):
    kast = randint(1,7)
    if kast == 6:
        seksere = seksere + 1

print("Relfrek:", seksere/N,
      "Sannsynlighet:", 1/6)
        
        
        
        
        
        
