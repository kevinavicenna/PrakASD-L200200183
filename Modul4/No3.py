from mhs import MhsTIF,Daftar,c0

def CariNilaiTerkecilBanyak(list):
    k = c0.ambilUangSaku()
    a = []
    for x in Daftar:
        if x.ambilUangSaku() < k:
            a.append((x.nama, x.NIM, x.kotaTinggal, x.uangSaku))
    return a


