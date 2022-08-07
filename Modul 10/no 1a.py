import time
from timeit import timeit

def jumlahkan_cara_1(n):
    x = 0
    for i in range(1, n+1):
        x = x + i
    return x

for i in range(5):
    a = 'from __main__ import jumlahkan_cara_1'
    j = jumlahkan_cara_1(1000000)
    t = timeit('jumlahkan_cara_1(2000000)', setup = a, number=1)
    print("Jumlah %d perlu %9.8f detik" % (j, t))
