import re

s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
print(cocok[0]) ## => ’dita-b@google.com
