import random
def tebak():
    x = random.randrange(1,101)
    b = -1
    n =0
    
    while x != b:
        n += 1
        b = int(input("masukan tebakan ke- "+str(n)+":>"))

        if b<x:
            print('Itu terlalu kecil.Coba lagi')
        elif b>x:
            print("itu terlalu besar.Coba lagi")
        else:
            print("Anda benar")
            break
tebak()