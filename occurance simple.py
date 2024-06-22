""" on se propose d'écrire un programme en python
    qui permet de :
    - lire une chaine ch non vide
    - lire un caractère c non vide de taille 1
    - calculer et afficher l'occurence de c dans ch """
# contrôle de saisie sur la chaine ch
ch = ""
while ch == "" :
    ch = input("entrer une chaine non vide : ")
# contrôle de saisie sur le caractère c
c = ""
while len(c) != 1 :
    c = input("entrer un caractère : ")
# initialisation du compteur occ
occ = 0
# parcour complet de la chaine ch
for i in range(0,len(ch)):
    if ch[i].upper == c.upper() :
        # incrementer occ
        occ = occ + 1
# afficher le résultat
print ("l'occurence de \"",c,"\" dans \"",ch, "\" est : ",occ)