#somme dès le début
s = 0
n = int(input("Entrer un nombre: "))
ch = ""
for i in range(1, n + 1, 1):
    ch = ch + str(i) + "+"
    s += i 
print(ch[:len(ch)-1]+" =", s)