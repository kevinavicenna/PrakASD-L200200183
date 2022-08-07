def apakahTerkandung(a,b):
       # for i in a:
        #    if i in b:
         #       print("True")
         #   else:
         #       print("False")
    y = True
    for i in range(len(b)):
        if a in b:
            y = True
        else:
            y = False
    return y

print(apakahTerkandung("halo","h"))

