from LatOOP3 import Manusia
from N import Mahasiswa
 
class MhsTIF(Mahasiswa):
    def sss():
        return "L"
    #def __init__(self,nama,norumah,kota,sangu):
    #    self.nama = nama
    #    self.norumah = norumah
    #    self.kota = kota
    #    self.sangu = sangu

    #def __str__(self):
    #    identitas = self.nama +" ,no rumah "+ str(self.norumah) \
    #    + "bertempat kota "+str(self.kota) \
    #    +"uang nya "+ str(self.sangu)
    #    return identitas

    #def ambilNama(self):
    #    return self.nama
    #def norumah(self):
    #    return self.norumah
    #def kotaTinggal(self):
    #    return self.kota
    #def ambilSangu(self):
    #    return self.sangu

c0 = MhsTIF("k",10,"Klaten",2222222)
c1 = MhsTIF("v",23,"SKA",22)
c2 = MhsTIF("ee",22,"SKO",2222)

Daftar=[c0,c1,c2]

target = "Klaten"
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + "tingggal"+target)
