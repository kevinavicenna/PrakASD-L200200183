from time import time as detak
from random import shuffle as s
import no5  
import no6 
import no3  
k = [i for i in range(1, 6000)]
s(k)

merA = k[:]
merB = k[:]
quiA = k[:]
quiB = k[:]

# merge Sort baru
aw = detak();
no5.merge_sort(merB);
ak = detak();
print('merge sort baru : %g detik' % (ak-aw))

# Quick Sort baru
aw = detak();
no6.quickSort(quiB);
ak = detak();
print('quick sort baru : %g detik' % (ak-aw))

# Merge Sort dan Quick Sort Awal
aw = detak(); 
no3.mergeSort(merA); 
ak = detak(); 
print('merge sort Awal : %g detik' % (ak-aw))

aw = detak();
no3.quickSort(quiA); 
ak = detak();
print('quick sort Awal : %g detik' % (ak-aw))
