def formatrupiah(uang):
    x = str(uang) 
    if len(x) <= 3 :
        return 'Rp ' + x    
    else :
        p = x[-3:]
        q = x[:-3]
        return   formatrupiah(q) + '.' + p
        print('Rp ' +  formatrupiah(q) + '.' + p)

print(formatrupiah(2000000))