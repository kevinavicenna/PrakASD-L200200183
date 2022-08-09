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

pesanA = Pesan(999)
print(pesanA.teks)

pesanA.cetakIni()
