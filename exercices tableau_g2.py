from numpy import array
N=""
while not N.isdigit() or int(N) < 5 or int(N) > 10 :
    N = input("entrer la taille du tableau (5,10): ")
N = int(N)
T = array([0]*N)
print(T)
for i in range (N):
    T[i]=input("enter le "+ str(i+1)+"  element du tableau")
print(T)