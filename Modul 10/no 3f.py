import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        for j in range(i):
            for k in range(j):
                x = i + j + k + 2019
        
def ujiKalangBersusuh(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import kalangBersusuh'
    for i in jangkauan:
        print('i = ',i)
        t = timeit.timeit('kalangBersusuh(' + str(i) +')', setup = siap,number=1)
        ls.append(t)
    return ls

n = 10
LS = ujiKalangBersusuh(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
