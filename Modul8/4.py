class Queue(object):
    def __init__(self):
        self.qlist = []
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)

    # FUNGSI untuk mengetahui yg paling dpn tanpa menghapus 
    # dan mengetahui item yg paling belakang tanpa menghapus    
    def getFrontMost(self): 
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[0]
    def getRearMost(self):  
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[-1]
    
c = Queue()
c.enqueue(28)
c.enqueue(19)
c.enqueue(45)
c.enqueue(13)
c.enqueue(7)

print (c.qlist)
print ("Item terdepan : " , c.getFrontMost())
print ("Item terbelakang : " , c.getRearMost())

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def getFrontMost(self):
        x = 0
        while self.qlist[x].priority != 0:
            x+=1
        return self.qlist[x].item

    def getRearMost(self):
        tmp = []
        for i in self.qlist:
            tmp.append(i.priority)
        print (self.qlist[tmp.index(max(tmp))].item)

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


d = PriorityQueue()
d.enqueue("Jeruk", 4)
d.enqueue("Tomat", 2)
d.enqueue("Mangga", 0)
d.enqueue("Duku", 5)
d.enqueue("Pepaya", 2)

print (d.qlist)
print ("Item paling depan : " , d.getFrontMost())
print ("Item paling belakang : " , d.getRearMost())

