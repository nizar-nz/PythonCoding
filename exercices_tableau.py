from numpy import array
N = ""
while not N.isdigit() or int(N) < 5 or int(N) > 10 : 
    N = input("donner la taille du tableau(5,10): ")
N = int(N)
T = array([int]*N)
for i in range(N):
    T[i]=int(input("donner l' "+str(i+1)+"ème entier du tableau: "))
print(T)