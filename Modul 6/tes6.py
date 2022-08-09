A = [2,3,4,56]
B = [2,3,5]

def gabunganDuaListUrut(A,B):
    la =len(A); lb = len(B)
    C = list()
    i = 0; j = 0

    while i < la and j < lb:
        if A[i] < B[j]:
            C.appAkhir(A[i])
            i += 1

        else:
            C.appAkhir(B[j])
            j+=1

    while i < la:
        C.appAkhir(A[i])
        i += 1

    while j < lb:
        C.appAkhir(B[j])
        j += 1

    return C
