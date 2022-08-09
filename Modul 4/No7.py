List = [2, 3, 4, 4, 5, 6, 6, 6, 8, 9, 9, 10,11,11,11,11, 12, 12,12,13,13, 13,14, 14,15]
def binSe2(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    a = []
    
    while low <= high:
        if kumpulan[low] == target:
            a.append(low)
            low += 1
        else:
            low += 1
    return a
