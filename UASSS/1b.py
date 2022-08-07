import re

f = open("helpre.txt",'r',encoding='latin1')

teks = f.read()
f.close()

cocok = re.findall(r"dia\w+", teks)
print(cocok)


import re

string = "Kevin Avicenna ,kevinavicenna@gmail.com"

name = re.findall(r'[\w\.-]+@[\w\.-]+',string)
for i in name:
    print(i)
