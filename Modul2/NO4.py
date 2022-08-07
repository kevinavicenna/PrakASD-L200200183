from LatOOP3 import Manusia
class Mahasiswa(Manusia):
        def __init__(self,nama,NIM,kota,us,matakuliah = []):
            self.nama = nama
            self.NIM = NIM
            self.kotaTinggal = kota
            self.uangSaku = us
            self.matakuliah = matakuliah
        def __str__(self):
            s = self.nama + ', NIM ' + str(self.NIM) \
                + '. Tinggal di ' + self.kotaTinggal \
                + '. Uang saku Rp ' + str(self.uangSaku) \
                + ' tiap bulannya.'
            return s
        def ambilNama(self):
            return self.nama
        def ambilNIM(self):
            return self.NIM
        def ambilUangSaku(self):
            return self.uangSaku
        def makan(self,s):
            print("Saya baru saja makan",s,"sambil belajar.")
            self.keadaan = 'kenyang'

        def listKuliah(self):
            return self.matakuliah
        def ambilKuliah(self, matakuliah):
            self.matakuliah.append(matakuliah)

        def hapuskuliah(self, matakuliah):
            self.matakuliah.remove(matakuliah)  
