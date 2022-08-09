class Mahasiswa:
    keadaan = 'lapar'
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' perharinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print('Saya baru aja makan', s, 'sambil nugas')
        self.keadaan = 'kenyang'

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)
        i = 0
        j = 0
        k = 0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i += 1
            else:
                A[k] = separuhkanan[j]
                j += 1
            k += 1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i += 1
            k += 1
        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j += 1
            k += 1

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)

def quickSortBantu(A, Awal, Akhir):
    if Awal < Akhir:
        titikBelah = partisi(A, Awal, Akhir)
        quickSortBantu(A, Awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, Akhir)
        
def partisi(A, Awal, Akhir):
    nilaiPivot = A[Awal]
    penandaKiri = Awal + 1
    penandaKanan = Akhir
    selesai = False
    while not selesai:
        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1
        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan -= 1
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp
    temp = A[Awal]
    A[Awal] = A[penandaKiri]
    A[penandaKanan] = temp
    return penandaKanan


mhs1 = Mahasiswa("Kevin", 183, "Surakarta", 9999999)
mhs2 = Mahasiswa("Azril", 202, "Denpasar", 9900000)
mhs3 = Mahasiswa("Aziz", 180, "Karanganyar", 555000)
mhs4 = Mahasiswa("Sheha", 189, "Ngawi", 155000)
mhs5 = Mahasiswa("Rohman", 135, "Denpasar", 20000000)

X = [mhs1.nim, mhs2.nim, mhs3.nim, mhs4.nim, mhs5.nim]
mergeSort(X)
print(X)
