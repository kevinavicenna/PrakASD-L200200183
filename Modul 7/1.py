import re

s = 'sebuah contoh KATA:teh!!'
cocok = re.findall(r'KATA:\w\w\w', s)

# Pernyataan-IF sesudah findall() akan memeriksa apakah pencarian berhasil: 4
if cocok:
    print('menemukan', cocok ) ## ’menemukan [kata:teh]’
else:
    print('tidak menemukan')
