class DataManusia():
    def __init__(self,nama,umur,warnakulit):
        self.nama = nama
        self.umur = umur
        self.warnakulit = warnakulit
    def dataNama(self):
        return "Nama = "+self.nama
    def dataUmur(self):
        return "Umur = "+ self.umur
    def dataWarnakulit(self):
        return "Warna Kulit = "+self.warnakulit

M1 = DataManusia("Kevin Avicenna",20,"sawo")
M2 = DataManusia("Azril",30,"sawo")
M3 = DataManusia("Aman",25,"sawo")
M4 = DataManusia("Aziz",26,"sawo")
M5 = DataManusia("Faris",21,"sawo")
M6 = DataManusia("Albert Enstain",20,"sawo")
M7 = DataManusia("Farid",20,"sawo")
M8 = DataManusia("Killua",12,"putih bening")
M9 = DataManusia("Eren",20,"putih")
M10 = DataManusia("Mikasa",20,"putih")

simpan = [M1,M2,M3,M4,M5,M6,M7,M8,M9,M10]

for i in simpan:
    print(i.nama,i.umur,i.warnakulit)



def cariwk(data,cari):
    d = []
    for i in data:
        if i.warnakulit ==cari:
            print(i.nama,i.umur,i.warnakulit)

def mergeSort(A) :
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j=0 ; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].umur < separuhKanan[j].umur:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j = j + 1
            k = k + 1
            
def metodemergesort(x):
    for i in x:
        print(i.nama,i.umur,i.warnakulit)
