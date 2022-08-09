import re

f = open("E:\PRAK ASD\Modul7\Indonesia.txt")
#f = open("E:\PRAK ASD\Modul7\Indonesia.txt", 'r', encoding='latin1')
x = []
teks = f.read()
f.close()

p = r'\s([Mm]e\w+)'
cocok = re.findall(p, teks)
x.append(cocok)
print(x)
