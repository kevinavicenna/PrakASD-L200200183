class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    def dequeue(self):
        tmp = []
        for i in self.qlist:
            tmp.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if tmp[i].priority < tmp[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item


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

print (d.dequeue())
print (d.dequeue())
print (d.dequeue())
print (d.dequeue())
print (d.dequeue())
