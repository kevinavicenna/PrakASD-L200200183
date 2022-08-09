import re

f = open("E:\PRAK ASD\Modul7\kei.html", 'r', encoding='latin1')

teks = f.read()
f.close()

i = r'\s<td>[\d\.\w\/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d\.\w\/]+)</td>'
IN = re.findall(p, teks)
x = [(i[0], float(i[1])) for i in IN]
print(x)
