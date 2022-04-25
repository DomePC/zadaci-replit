#Upiši šifru. Ako se šifra poklapa sa šifrom #123Replit onda ispiši lozinka je točno upisana ako ne zadtraži korisnika za ponovni unos. Treba se koristiti while petljom!

sifra = input("Upisi lozinku: ")

while(sifra != "#123Replit"):
  print("Pokusaj ponovo!")
  sifra = input("Upisi lozinku: ")

else:
  print("Lozinka je tacno upisana!")
