from mhs import MhsTIF,Daftar

def cariUangSakuKurangDari250000(list):
    nilai = 250000
    for x in Daftar:
        if x.ambilUangSaku() < nilai:
            print(x.ambilNama())

