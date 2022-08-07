from timeit import timeit
import random

print("\nskenario kasus rata-rata")
for i in range(5):
    g = list(range(2500))
    random.shuffle(g)
    t = timeit('sorted(g)', setup = 'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(g), t))

print("\nskenario kasus terburuk")
for i in range(5):
    g = list(range(2500))
    g = g[::-1]
    t = timeit('sorted(g)', setup = 'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(g), t))

print("\nskenario kasus terbaik")
for i in range(5):
    g = list(range(2500))
    t = timeit('sorted(g)', setup = 'from __main__ import g', number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(g), t))
