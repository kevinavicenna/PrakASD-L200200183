def cari(wadah,target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

A = [21,33,45]
X = cari(A,21)
print(X)
print(cari(A,21))
