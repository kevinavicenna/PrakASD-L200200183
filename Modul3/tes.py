class Node(object):
    """TESSS"""
    def __init__(self,data):
        self.data = data
        self.next = None
        
def kunjungi(head):
    curNode  = head
    while curNode is not None :
        print(curNode.data)
        curNode = curNode.next
