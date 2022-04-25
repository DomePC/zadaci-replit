
#Napiši program koji će unositi brojeve sve dok nije unesen negativan broj (while petlja). Nakon toga program provjerava da li je suma znamenki unesenih brojeva djeljiva s 3 te ispisuje one brojeve kojima je ovaj uvjet istinit. (brojevi idi do troznamenkastog)
#znamenka = broj % 10
#broj = broj // 10 - zaokružuje na najmanji sljedeći cijeli broj ali ipak dijeli s 10

while True:
    n = int(input('Unesi broj: '))
    if n < 0:
        break
    else:
        broj = n
        suma = 0
        while broj > 0:
            znam = broj % 10
            suma = suma + znam
            broj = broj // 10

            if suma % 3 == 0:
                print(n)