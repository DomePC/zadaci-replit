#1.Tražiti od korisnika unos broja u rasponu od 10-20. Ukoliko korisnik pogodi raspon; ispisati:
#cestitamo-unijeli ste broj u rasponu i ispisati broj kojeg je korisnik unio. Ako korinsik ne
#pogodi broj, ispisati: broj nije u rasponu od 10-20; Pokušajte ponovno. Petlja se izvršava
#tako dugo dok je uvjet na TRUE odnosno dok korisnik unosi brojeve veće od nula. Ako
#koirsnik unese 0 odnosno FALSE, prekida se izvođenje programa.

n = int(input("Unesite broj izmedju 10 i 20: "))

while n not in range(10, 20):
  print("Niste uneli broj izmedju 10 i 20 ili niste pogodili!")
  n = int(input("Unesite broj i pokusajte ponovo: "))
  if(n == 0):
    break
else:
  print("Cestitamo uneli ste broj u rasponu " + str(n))

