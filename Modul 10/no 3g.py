import timeit
import matplotlib.pyplot as plt

def kalangBersusuh(n):
    for i in range(n):
        if i % 3 == 0:
            for j in range(n // 2):
                j += j
        elif i % 2 == 0:
            for j in range(5):
                j += j
        else :
            for j in range(n):
                j += j
        
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
