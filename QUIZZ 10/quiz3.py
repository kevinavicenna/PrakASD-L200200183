from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(5)
root.right.right.right = Node(8)
root.right.right.right.left = Node(6)
root.right.right.right.right = Node(10)
print(root)

# def preorderTrav(subpohon):
#     if subpohon is not None:
#         print(str(subpohon.data)+"->",end='')
#         preorderTrav(subpohon.kiri)
#         preorderTrav(subpohon.kanan)
# preorderTrav(root)