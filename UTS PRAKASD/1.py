def persegi():
    """Persegi"""
    print("program menghitung luas persegi panjang")
    a = int(input("Masukan nilai integer sisi "))
    return "Luas persegi nya adalah "+str(a*a)

def lingkaran():
    """Lingkaran"""
    print("program menghitung luas lingkaran")
    a = int(input("masukan nilai integer jari-jari "))
    if a % 7 ==0:
        b=22/7
    else:
        b=3.14
    return"Luas lingkaran nya adalah "+str(b*a*a)


def segitigaSamaSisi():
    """Segitiga Sama Sisi"""
    print("Program menghitung Luas Segitiga Sama SIsi")
    alas = int(input("Masukan Alas Segitiga "))
    tinggi = int(input("Masukan tinggi Segitiga "))
    return "Luas Segitiga Sama Sisi nya Adalah " + str(1/2*alas*tinggi)


def belahKetupat():
    print("Program menghitung Luas Belah Ketupat")
    d1 = int(input("Masukan nilai d1 "))
    d2 = int(input("Masukan nilai d2 "))
    return "Luas Belah Ketupat " + str(1/2*d1*d2)

