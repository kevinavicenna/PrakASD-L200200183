import re 

#teks = 'kevin123'
cocok = re.findall(r'\d\d','t123h di 2019 bulan 023')

if cocok:
    print('menemukan bruh',cocok)
else:
    print('ranek')
