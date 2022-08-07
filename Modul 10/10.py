import time
import random

##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1,n+1):
##        hasilnya = hasilnya +i
##    return hasilnya
##def jumlahkan_cara_2(n):
##    return(n*(n+1))/2
##
##for i in range(5):
##    awal =time.time()
##    h = jumlahkan_cara_1(10000)
##    akhir = time.time()
##    print("Jumlah adalah %d,memerlukan %19.10f detik" %(h,akhir-awal))
##
##print("\nCara 2\n")
##
##for i in range(5):
##    awal =time.time()
##    h = jumlahkan_cara_2(10000)
##    akhir = time.time()
##    print("Jumlah adalah %d,memerlukan %20.10f detik" %(h,akhir-awal))
##

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai

##for i in range(5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7 detik" % (len(L),akhir-awal))

##for i in range(5):
##    L = list(range(3000)) 3 L = L[::-1] # Membalik urutan elemen di list 4 awal = time.time() 5 U = insertionSort(L) 6 akhir = time.time() 7 print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L)

import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range(n):
            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan = range(1,n+1)
    siap = "from __main import kalangBerususuh"
    for i in jangkauan:
        print('i = ',i)
        t=timeit.timeit("kalangBersusuh("+str(i)+")",setup = siap,number = 1)
        ls.append(t)
    return ls

n = 1000
LS = ujiKalangBersusuh(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1,n+1)])
plt.show()
