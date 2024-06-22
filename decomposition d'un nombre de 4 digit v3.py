'''écrire un programme qui permet de saisir un nombre de n chiffres,
le décompose puis afficher le résultat'''

nbre = int(input ("saisir un nombre : "))
while not(nbre in range (10000000)) : #nombre de 0 à 9999999
    nbre = int(input ("saisir un nombre : "))
L = ["unités","disaines","centaines","milliers", "disaines de milliers", "centaines de milliers", "millions"]
ch = str(nbre)              # convertir le nombre en chaine 
for i in range(len(ch)):    # parcourir la chaine caractère par caractère
    print( "le nombre des ",L[i]," "*(21-len(L[i])), " est : ", int(ch[(len(ch)-i)-1]))