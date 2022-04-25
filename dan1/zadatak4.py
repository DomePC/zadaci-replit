#Napravi niz od random brojeva koristeći library random. Neka budu cijeli brojevi te neka ih u nizu bude 10. Potrebno je tada ispisati dvije stvari, parne i neparne brojeve. Format je sljedeći:
#Niz:
#Parni brojevi: broj1 broj2 ...
#Ne Parni brojevi: broj1 broj2...

import random

A = []
parni = []
neparni = []


for i in range(10):
  B = random.randint(0, 100)
  A.append(B)

for j in range(10):
  if A[j] % 2 == 0:
    parni.append(A[j])
  elif A[j] % 2 == 1:
    neparni.append(A[j])

print("Niz: " + str(A))
print("Parni su: " + str(parni))
print("Neparni su: " + str(neparni))