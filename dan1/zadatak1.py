#Unijeti 10 cijelih brojeva u niz te ispisati taj niz. Pritom je potrebno pronaci najmanji clan nize i najveci clan niza. Ispis treba biti u sljedećem formatu:
#Unesi 1..2..3 clan niza: unosimo clanove
#Upisani niz:
#Maksimum niza:
#Minimum niza:



lista = [];

for i in range(10):
    item = int(input("Unesi " + str(i+1) + " clan niza: "))
    lista.append(item)

max = max(lista)
min = min(lista)

print("Niz:", str(lista))
print("Maksimum niza:", str(max))
print("Minimum niza:", str(min))