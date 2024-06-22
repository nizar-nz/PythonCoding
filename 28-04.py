'''
Ecrire un script python qui demande à l’utilisateur
de saisir un nombre formé de deux chiffres distincts,
de déterminer et d’afficher la somme de ses chiffres 
ainsi que son inverse.
'''
nbr =''
while not nbr.isdigit() or len(nbr) !=2 or nbr[0]==nbr[1] :
  nbr = input("saisir un nombre formé de deux chiffres distincts: ")
print ("la somme de ses chiffres de",nbr,"est:",int(nbr[0])+int(nbr[1]))
print("l'inverse de",nbr,"est:",nbr[1]+nbr[0])