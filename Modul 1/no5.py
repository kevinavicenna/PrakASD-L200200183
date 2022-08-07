from math import sqrt as sq

def apakahPrima(n):
    n = int(n) # Kalau pecahan, dibuang pecahannya.
    assert n>=0 # Hanya menerima bilangan non-negatif. 
    primaKecil = [2,3,5,7,11] # Kalau angkanya kecil, akan 
    bukanPrKecil = [0,1,4,6,8,9,10] # tertangkap di sini. 
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%i==0:
                return False
            return True

print(apakahPrima(17))