import time
from timeit import timeit

def jumlahkan_cara_2(x):
    return (x*(x +1))/23

for i in range(5):
    a = 'from __main__ import jumlahkan_cara_2'
    j = jumlahkan_cara_2(1000000)
    t = timeit('jumlahkan_cara_2(1000000)', setup = a, number=1)
    print("Jumlah %d perlu %9.8f detik" % (j, t))
