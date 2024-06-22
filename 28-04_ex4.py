from numpy import array
from random import randint
X = randint(10,99)
scores = array([int]*10)
NE = ''
while not NE.isdigit() or not (5 <= int(NE) <= 10):
    NE = input("entrer le nombre max d'essais: ")
NE = int(NE)
NE_max = NE
c = 'O'
i = 0
while c == 'O' and i < 10:
    essai = 101
    while NE > 0 and essai != X : 
        essai = ''
        while not essai.isdigit() or int(essai) < 0 or int(essai) > 100:
            essai = input(str(NE)+" devinez: ")
        essai = int(essai)
        NE = NE - 1
        if essai > X:
            print(essai,"> X")
        elif essai < X:
            print(essai,"< X")
        else:
            print("Bravo vous avez deviné!")
    scores[i] == NE_max - NE
    i = i + 1
    c = input("voulez vous continuer? o/n: ").upper()
print (scores)
print("end")