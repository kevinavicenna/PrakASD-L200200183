def rerata(x):
    jumlah = 0 
    for i in range(len(x)):
        jumlah += x[i]
    jumlah = jumlah/len(x)
    return jumlah

print(rerata([1,2,3,4,5]))