def bilanganPrima(x):
    for i in range(2,x):
        prima = True
        for j in range(2,i):
            if(i%j==0):
                prima=False
        if(prima):
            print(i)
print(bilanganPrima(100))