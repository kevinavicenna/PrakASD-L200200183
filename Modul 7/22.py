import re

f = open('indonesia.txt', 'r', encoding='latin1')

x = []
teks = f.read()
f.close()

p = r'\s(di\w+)'
cocok = re.findall(p, teks)
x.append(cocok)
print(x)

