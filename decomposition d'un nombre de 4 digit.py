'''écrire un programme qui permet de saisir un nombre de quatre chiffre,
le décompose puis afficher le nombre des milliers, des centaines,
des disaines et des unités''' 
valide = False         #condition d'entrer dans la boucle
while not(valide) :    #tant que ce n'est pas valide répéter 
    nbre = int(input ("saisir un nombre de 4 chiffre : ")) 
    valide = (1000 <= nbre <= 9999)    # contrôle de saisie
M = nbre // 1000                       #milliers
C = (nbre - (M*1000)) // 100           #centaines
D = (nbre - ((M*1000)+(C*100))) // 10  #disaines
U = nbre - ((M*1000)+(C*100)+(D*10))   #unités
# affichage de résultat
print ("le nombre des unités    est : ",U)
print ("le nombre des disaines  est : ",D)
print ("le nombre des centaines est : ",C)
print ("le nombre des milliers  est : ",M)


