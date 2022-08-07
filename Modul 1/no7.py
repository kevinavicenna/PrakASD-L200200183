def faktorisasiprima(x):
    
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

print(faktorisasiprima(10))
