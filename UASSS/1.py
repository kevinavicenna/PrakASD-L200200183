##import re
##
##f = open("helpre.txt")
##
##T = []
##teks = f.read()
##f.close()
##
##p = r'\s([Dd]ia\w+)'
##cocok = re.findall(p, teks)
##T.append(cocok)
##print(T)


import re

teks = ''' kevinavicenna@gmail.com '''

t = re.findall(r'\w',teks)
for i in t:
    for a in i:
        print(a)
