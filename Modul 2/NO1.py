class Pesan(object):
    """
            Tes class
    """

    def __init__(self,stringg):
        self.teks = stringg 
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai " ,len(self.teks),"karakter.")
    def perbarui(self,stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self,a):
        if a in self.teks:
            return True
        else:
            return False

    def hitungKonsonan(self):
        k = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        x = 0
        
        for i in self.teks:
            if i in k:
                x += 1
        return x
    
    def hitungVokal(self):
        v = 'aiueoAIUEO'
        x = 0
        
        for i in self.teks:
            if i in v:
                x += 1
        return x
