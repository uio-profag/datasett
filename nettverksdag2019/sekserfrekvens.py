from pylab import *

seksere = 0
enere = 0
N = 100000 # Antall kast

for i in range(N):
    kast = randint(1,7)
    if kast == 1:
        enere += 1
    elif kast == 6:
        seksere += 1

print("Antall enere:", enere,
      "Antall seksere:", seksere,
      "Frekvens seksere:", seksere/N,
      "Sanns. sekser:", 1/6)
