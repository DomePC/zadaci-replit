#Napraviti kalkulator. Koristiti se svim osnovnim operacijama kao monzenje, zbrajanje, oduzimanje itd. Korisnik mora izabrati preko izbornika što će raditi to jest koju će matematičku operaciju koristiti. Kako je ovo jednostavan kalkulator neka se koriste samo dva broja za izvršenje operacija!



a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))

print("Mogunosti : 1. Sabiranje, 2. Oduzimanje, 3. Deljenje, 4. Mnozenje")

n = int(input())

if(n == 1):
  print("Zbir je: " + str(a+b))
elif(n == 2):
  print("Razlika je: " + str(a-b))
elif(n == 3):
  print("Cinilac je: "+ str(a*b))
elif(n == 4):
  print("Deljenik je: " + str(a/b))
else:
  print("Niste uneli operaciju!")



