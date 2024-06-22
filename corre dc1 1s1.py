print("Bonjour, je m'appelle scratchy et j'ai appris la table de multiplication!")
n = int(input("Entrer un nombre entre 1 et 10 "))
if n < 1 or n > 10 :
    print("Erreur de saisie, veuillez réexécuter le programme!")
else :
    i = 1
    while not ( i > 10 ):
        print(str(n) + ' * ' + str(i) + ' = ' + str(n*i))
        i = i + 1