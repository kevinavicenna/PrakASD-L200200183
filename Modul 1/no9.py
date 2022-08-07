def kelipatan(a):
    for i in range(a):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print("Python UMS")
        elif(i%3==0):
            print("Python")
        elif(i%5==0):
            print("UMS")
        else:
            print(i)

print(kelipatan(10))