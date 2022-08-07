#No 1
class Simpul(object):
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = Simpul("L200200183")
B = Simpul("L200200184")
C = Simpul("L200200185")
D = Simpul("L200200186")
E = Simpul("L200200187")
F = Simpul("L200200188")

A.kiri = B
A.kanan = C
B.kiri = D
B.kanan = E
C.kiri = F

def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.kiri)
        preorder(root.kanan)

def inorder(root):
    if root is not None:
        inorder(root.kiri)
        print(root.data)
        inorder(root.kanan)

def postorder(root):
    if root is not None:
        postorder(root.kiri)
        postorder(root.kanan)
        print(root.data)

preorder(A)
#inorder(A)
#postorder(A)

