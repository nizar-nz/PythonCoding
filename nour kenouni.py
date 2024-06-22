from numpy import array
from random import randint
N=10
T=array ([int]*N)
for i in range (N):
    T[i]=randint(-9,9)
print (T)
for i in range (N):
    if T[i]<0:
        T[i]=T[i]+5
    else:
        T[i]=T[i]-5 
print(T)
