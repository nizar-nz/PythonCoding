Totaltentatives=7
essai=1
from random import randint
NbrMystere =randint(0,100)
tentative= int(Totaltentatives -1)
print("j'ai fixer un nombre aletoire entre 0 et 100")
print("Ta mission est de retrouver en ", Totaltentatives, "essais")
while not (tentative == NbrMystere or essai> Totaltentatives) :
    input("essai n°" + str(essai) + "devinez")
    reponse = tentative
    if tentative > NbrMystere :
        print("le nombre recherché est plus petit que",tentative)
    elif tentative < NbrMystere :
        print("le nombre recherché est plus grand que " , tentative)
    essai = int(essai +1)
if tentative ==NbrMystere :
    print("bravo!")
else :
    print("Dommage:-(")
