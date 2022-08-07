class node(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def carilinkedlist(self, dicari):
        cur = self
        while cur is not None:
            if cur.next != None:
                if cur.data != dicari:
                    cur = cur.next
                else:
                    print ("Data", dicari, "terdapat di Linked List")
                    break
            elif cur.next == None:
                print ("Data", dicari, "terdapat di Linked List")
                break

