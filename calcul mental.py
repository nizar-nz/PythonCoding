from random import randint
a = randint(1,100)
b= randint(1,100)
print("Bonjour, aujourd'hui on testera le calcul mental")
les_tentatives_possibles = 3
numero_essai = 1
s = 0
while s != a + b and numero_essai <= les_tentatives_possibles :
    s = int(input("donner le résultat de la somme de : " + str(a) + " + " + str(b) + " = "))
    if s == a + b :
        print("Bravo!")
    else :
        print("incorrecte! :-(")
    numero_essai = numero_essai + 1
