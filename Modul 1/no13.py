def Terbilang(angka):
    x=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]

    Hasil=" "
    n = int(angka)
    if n >= 0 and n <= 11:
        Hasil = Hasil + x[n]
    elif n < 20:
        Hasil = Terbilang(n%10) + " Belas"
    elif n < 200:
        Hasil = Terbilang(n/10) + " Puluh"+Terbilang(n%100)
    elif n < 200:
        Hasil = " Seratus"+Terbilang(n-100)
    elif n < 1000:
        Hasil = Terbilang(n/100) + " Ratus"+Terbilang(n%100)
    elif n < 2000:
        Hasil = "Seribu"+Terbilang(n-1000)
    elif n < 10000:
        Hasil = Terbilang(n/1000) + " Ribu"+Terbilang(n%1000)
    elif n < 20000:
        Hasil = "Sepuluh Ribu"+Terbilang(n-10000)
    elif n < 100000:
        Hasil = Terbilang(n/10000) + " Puluh"+Terbilang(n%10000)
    elif n < 200000:
        Hasil = "Seratus"+Terbilang(n-100000)
    elif n < 1000000:
        Hasil = Terbilang(n/100000) + " Ratus"+Terbilang(n%100000)
    elif n < 2000000:
        Hasil = "Satu juta"+Terbilang(n-1000000)
    elif n < 10000000:
        Hasil = Terbilang(n/1000000) + " Juta"+Terbilang(n%1000000)
    elif n == 10000000:
        Hasil ="Satu Milyar"+Terbilang(n%10000000)
    else:
        Hasil="Angka hanya sampai satu milyar"
    return Hasil

print(Terbilang(23000))