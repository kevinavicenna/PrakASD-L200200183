from LatOOP3 import Manusia
class Mahasiswa(Manusia):
     def __init__(self,NAMA,NIM,KOTA,US):
          self.nama = NAMA
          self.NIM = NIM
          self.kotaTinggal = KOTA
          self.uangSaku = US
          
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
          print("Saya makan",s,"sambil belajar.")
          self.keadaan = 'kenyang'

          
     def ambilKotaTinggal(self):
          return self.kotaTinggal
     def perbaruiKotaTinggal(self, x):
        self.kotaTinggal = x
     def tambahUangSaku(self, uang):
        self.uangSaku = self.uangSaku + uang



          
