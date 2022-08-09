def cariWarnaKulit(data,warna):
    hasil = []
    for a in data:
        if a.dataWarnakulit() == warna:
            hasil.append(str(a.dataNama())+''+str(a.dataUmur()))
        return hasil
    print(cariWarnaKulit(data,'sawo'))