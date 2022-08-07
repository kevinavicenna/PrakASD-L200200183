from mhs import MhsTIF,Daftar,c0

def CariNilaiTerkecil(list):
    k = c0.ambilUangSaku()
    for x in Daftar:
        if x.ambilUangSaku() < k:
            k = x.ambilUangSaku()
    return k

