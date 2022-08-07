import re
f = open('indonesia.txt', 'r', encoding='latin1')
a = []
teks = f.read()
f.close()
p = r'\s([Mm]e\w+)'
cocok = re.findall(p, teks)
a.append(cocok)
print(a)
