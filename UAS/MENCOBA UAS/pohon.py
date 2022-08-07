from git import Object


class Simpul(Object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = Simpul('kevin')
B = Simpul('azril')
C = Simpul('Yudha')
D = Simpul('Ivan')
E = Simpul('Arsen')

A.kiri = B
A.kanan = C
B.kiri = D
B.kanan = E

def inorder(root):
    if root:
        inorder(root.kiri)
        print(str(root.data)+"->",end='')
        inorder(root.kanan)

inorder(A)
