kolicina = float(input("Unesi kolicinu valute: "))
trenutna_valuta = input("Unesi trenutnu valutu: ")
konverter_valuta = input("Unesi konverter valutu: ")

def HRK_to_USD(kolicina):
    if trenutna_valuta == "HRK" and konverter_valuta == "USD":
        kon_valuta = kolicina * 0.14
        print(round(kon_valuta, 2))

def HRK_to_EUR(kolicina):
    if trenutna_valuta == "HRK" and konverter_valuta == "EUR":
        kon_valuta = kolicina * 0.13
        print(round(kon_valuta, 2))

def EUR_to_HRK(kolicina):
    if trenutna_valuta == "EUR" and konverter_valuta == "HRK":
        kon_valuta = kolicina * 7.56
        print(round(kon_valuta, 2))

def USD_to_HRK(kolicina):
    if trenutna_valuta == "USD" and konverter_valuta == "HRK":
        kon_valuta = kolicina * 7.06
        print(round(kon_valuta, 2))

HRK_to_USD(kolicina)
HRK_to_EUR(kolicina)
EUR_to_HRK(kolicina)
USD_to_HRK(kolicina)

input('\n\npress ENTER to exit from the program')