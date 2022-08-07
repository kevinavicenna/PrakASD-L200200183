class _SimpulPohonBiner(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None
def ukuranpohon(root,count=0):
    if root is None:
        return count
    return ukuranpohon(root.kiri,ukuranpohon(root.kanan,count+1))

def tinggipohon(root):
    if root is None:
        return 0
    else:
        return max(tinggipohon(root.kiri),tinggipohon(root.kanan))+1

def cetak(root,count = 0 ):
    if root is not None:
        print(root.data + ',level '+str(count))
        (cetak(root.kiri,count+1),cetak(root.kanan,count+1))
#Membuat Simpul

A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

# tengah kiri kanan
def preorderTrav(root):
    if root is not None:
        print(str(root.data)+"->",end='')
        preorderTrav(root.kiri)
        preorderTrav(root.kanan)

print(preorderTrav(A))

# kiri tengah kanan
def inorderTrav(root):
    if root is not None:
        inorderTrav(root.kiri)
        print(str(root.data)+"->",end='')
        inorderTrav(root.kanan)
print(inorderTrav(A))

#kiri kanan tengah
def postorderTrav(root):
    if root is not None:
        postorderTrav(root.kiri)
        postorderTrav(root.kanan)
        print(str(root.data)+"->",end='')
