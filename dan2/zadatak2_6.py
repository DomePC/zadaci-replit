#Napisi program koji unosi osobno ime te ispisuje poruku je li ucitano ime musko ili zensko. Ako ime zavrsava slovom ’a’ ispisat ce se poruka ’Zensko ime’, a u svim ostalim slucajevima ’Musko ime’. Iznimke cemo zanemariti.

ime = input('Unesi svoje ime: ')
if ime[-1] == 'a':
    print('Žensko ime')
else:
    print('Muško ime!')