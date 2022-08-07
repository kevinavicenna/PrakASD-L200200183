from 1 import swap

X = [1,3,6,10,11,20]
Y = [7,8,9,12,13,100]
C = X + Y

def urut(a):
    n = len(a)
    for i in range (n-1):
        for j in range(n-i-1):
            if a[j]> a[j+1]:
                swap(a,j,j+1)