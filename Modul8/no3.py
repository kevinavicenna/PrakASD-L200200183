from no1 import Stack

S2 = Stack()         
for i in range (16) :    
    if i % 3 == 0:       
        S2.push(i)   
    elif i % 4 == 0:     
        S2.pop()      

print(S2.items)


