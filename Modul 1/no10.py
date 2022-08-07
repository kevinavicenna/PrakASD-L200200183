def selesaikanABC(a,b,c):
    sol = 0
    sol = (b**2)-(4*a*c)

    if sol == 0:
        print('Determinan nya nol, Persmaan mempunyai satu akar kembar.')
    elif sol > 0:
        print('Determinan positif, punya akar real dan berlainan.')
    elif sol < 0 :
        print("Determinan negatif, tidak mempunyai akar real ")

selesaikanABC(2,3,4)