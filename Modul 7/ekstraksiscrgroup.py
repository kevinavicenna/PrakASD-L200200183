s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'([\w.-]+)@([\w.-]+)', s)
## perhatikan posisi () di polanya 3 cocok ## adalah [(’dita-b’, ’google.com’)] 4 ## Bisa kita pilah satu per satu seperti ini: 5 cocok[0][0] ## ’dita-b’ 6 cocok[0][1] ## ’google.com’
