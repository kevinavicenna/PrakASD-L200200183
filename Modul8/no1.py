class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()
    def push(self, data):
        self.items.append(data)

def cetakHexa(b):
    S = Stack() #menyimpan class stack ke var S

    if b == 0:
        S.push(0)

    while b !=0:
        sisa = b%16
        b = b//16
        S.push(sisa)
        hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    
    hasil = ""
    
    for i in range (len(S)):
        hasil += str(hexa[S.pop()])
    
    return hasil

