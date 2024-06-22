'''écrire un programme qui permet de saisir un nombre de quatre chiffre,
le décompose puis afficher le nombre des milliers, des centaines,
des disaines et des unités'''

nbre = int(input ("saisir un nombre de 4 chiffre : "))
while not(nbre in range (1000,10000)) :   # contrôle de saisie
    nbre = int(input ("saisir un nombre de 4 chiffre : "))
    
M = nbre // 1000          #milliers
C = (nbre % 1000) // 100  #centaines
D = (nbre %100) // 10     #disaines
U = nbre % 10             #unités
#affichage des résultat
print ("le nombre des unités    est : ",U)
print ("le nombre des disaines  est : ",D)
print ("le nombre des centaines est : ",C)
print ("le nombre des milliers  est : ",M)



