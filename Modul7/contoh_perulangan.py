import re

## e+ = satu atau lebih e, sebanyak-banyaknya.
cocok = re.findall(r'te+', 'ghdteeeh') #=> cocok == [’teee’]

## Menemukan solusi yang paling kiri, dan dari situ mendorong si tanda ‘+’ 5
## sejauh-jauhnya (ingat ’paling kiri dan paling besar’).
## Pada contoh ini, perhatikan bahwa pencarian menemukan dua pola yang tepat.
cocok = re.findall(r'e+', 'teeheeee') #=> cocok == [’ee’, ’eeee’]

## \s* = nol atau lebih karakter putih (spasi, tab, dsb.)
## Di sini mencari 3 angka, kemungkinan dipisahkan oleh spasi/tab.
polanya = r'\d\s*\d\s*\d'
cocok = re.findall(polanya, 'xx1 2 3xx') #=> cocok == [’1 2 3’]
cocok = re.findall(polanya, 'xx12 3xx') #=> cocok == [’12 3’]
cocok = re.findall(polanya, 'xx123xx') #=> cocok == [’123’] 15

## ^ -> cocok dengan awal string, jadi ini tidak akan menemukan:
cocok = re.findall(r'^k\w+', 'mejakursi') #=> tidak ketemu, cocok == []

## tapi tanpa ^ dia berhasil:
cocok = re.findall(r'k[\w\s]+', 'mejakursi tamu saya') #=> cocok == ['kursi tamu saya']

s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'\w+@\w+', s)
print(cocok[0]) ## => ’b@google’
