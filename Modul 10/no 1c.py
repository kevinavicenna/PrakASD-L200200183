import random
from timeit import timeit

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos -1
        A[pos] = nilai


print("\nskenario kasus rata-rata")

for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(2500))
    random.shuffle(L)
    t = timeit('insertionSort(L)', setup = siap, number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(L), t))

print("\nskenario kasus terburuk")
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(2500))
    L = L[::-1]
    t = timeit('insertionSort(L)',setup = siap, number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(L), t))

print("\nskenario kasus terbaik")
for i in range(5):
    siap = 'from __main__ import insertionSort, L'
    L = list(range(2500))
    t = timeit('insertionSort(L)', setup = siap, number=1)
    print("Mengurutkan %d bilangan perlu %8.7f detik" % (len(L), t))
