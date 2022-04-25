#Napisi program koji iz liste imena = [’Pero’, ’Ivo’,’Ana’,’Katarina’,’Masa’,’Darko’,’Tin’] ispisuje najduzu rijec.

imena = ['Pero', 'Ivo','Ana','Katarina','Masa','Darko','Tin']

max_len = len(imena[0])

for i in range(len(imena)):
    if len(imena[i]) > max_len:
        max_len = len(imena[i])
        max_len_ime = imena[i]

print(max_len_ime)