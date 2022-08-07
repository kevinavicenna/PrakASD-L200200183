import re

f = open('E:\PRAK ASD\Modul7\Indonesia.txt', 'r', encoding='latin1')

x = []
teks = f.read()
f.close()

p = r'\s(di\s\w+)'
cocok = re.findall(p, teks)
x.append(cocok)
print(x)

