def jumlahHurufKonsonan(a):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    x = 0
    hasil = 0
    for i in a:
        if i in konsonan:
            x += len(i)
        else:
            x += 0
    hasil = len(a),x
    return hasil

print(jumlahHurufKonsonan("ayam"))