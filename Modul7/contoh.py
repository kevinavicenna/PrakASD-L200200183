1 ## Dua baris ini mencari pola ’eee’ di string ’teeeh’.
2 ## Seluruh pola harus cocok, tapi itu bisa muncul di mana saja.
3 ## Jika berhasil, \texttt{cocok} adalah daftar semua teks yang cocok.

import re

cocok = re.findall(r'eee', 'teeeh') #=>cocok == [’eee’] 
cocok = re.findall(r'ehs', 'teeeh') #=> cocok == []

## . = semua karakter kecuali \n
#cocok = re.findall(r'..h', 'teeeh') #=> cocok == [’eeh’] 

## \d = karakter angka, \w = karakter huruf atau angka
#cocok = re.findall(r'\d\d\d', 't123h di 2019 bulan 02') #=> cocok == [’123’, ’201’]
#cocok = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!') #=> cocok == [’def’, ’tgh’]

for a in cocok:
    print('menemukan', cocok ) ## ’menemukan [kata:teh]’
else:
    print('tidak menemukan')
