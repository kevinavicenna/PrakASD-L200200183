from mhs import MhsTIF,Daftar

def cariTempatTinggal(x):
    b = []
    for i in Daftar :
        if i.kotaTinggal == str(x):
            b.append(Daftar.index(i))
    return b
