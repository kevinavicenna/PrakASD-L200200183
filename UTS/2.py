def perkalian(x,y):
    hasil = []
    hitungmat1 = len(x) + len(x[0])
    hitungmat2 = len(y) + len(y[0])
    if hitungmat1 == hitungmat2:
        for i in range(0,len(x)):
            simpan = []
            for a in range(0,len(x[0])):
                jml = 0
                for b in range(len(x)):
                    jml += (x[i][b] * y[b][a])
                simpan.append(jml)
            hasil.append(simpan)
        return "Hasil Perkalian dengan ordo yang sama "+str(hasil)
    else:
        for i in range(len(x)):
            simpan = []
            for a in range(len(x[0])):
                jml = 0
                for b in range(len(y)):
                    jml += x[i][b] * y[b][a]
                simpan.append(jml)
            hasil.append(simpan)
        return "Hasil Perkalian Ordo berbeda "+str(hasil)
