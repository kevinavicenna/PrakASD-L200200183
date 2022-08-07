class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilKota(self):
        return self.kota
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten', 240000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def NIM_MHS(data):
    for i in data:
        print(i.NIM)
        
def Bubble_Sort(data):
    x = len(data)
    for i in range (x-1):
        for a in range(x-i-1):
            if data[a].NIM > data[a+1].NIM:
                swap(data,a,a+1)

X = [2,3,6,7,8,9,11,15,16]
Y = [20,22,45,66,77]
C = X + Y

def mengurutkan(a):
    q = len(a)
    for i in range (q-1):
        for j in range(q-i-1):
            if a[j]> a[j+1]:
                swap(a,j,j+1)



