import time
from timeit import timeit

def jumlahkan_cara_1(n):
    x = 0
    for i in range(1, n+1):
        x = x + i
    return x

for i in range(10):
    a = time.time()
    j = jumlahkan_cara_1(1000000)
    t = time.time()
    print("Jumlah %d perlu %9.8f detik" % (j, t))
