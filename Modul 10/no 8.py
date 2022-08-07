import timeit
import time
import matplotlib.pyplot as plt

def straight(cont, target):
    x = len(cont)
    for i in range(x):
        if cont[i] == target:
            return True
        return False

def tim():
    a = 100
    b = [12, 3, 5, 6, 8, 2, 11]
    awal = time.time()
    U = straight(b, a)
    akhir = time.time()
    print('Worst case')
    print('mengurutkan %d bilangan perlu %8.7f detik' % (U, akhir-awal))

tim()
tim()

def kalangBersusuh(n):
    a = 100
    b = [12, 3, 5, 6, 8, 2, 11]
    U = straight(b, a)

def ujiKalangBersusuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import kalangBersusuh'
    for i in jangkauan:
        print('i = ', i)
        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap, number=1)
        ls.append(t)
    return ls

n = 100
LS = ujiKalangBersusuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
