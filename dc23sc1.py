nom,dn,sy,de = "","","",""
while nom == "" :
    nom = input("entrer un nom: ")
while dn == "" :
    dn = input("entrer une date de naissance (jj-mm-aaaa): ")
while len(sy) != 2 :
    sy = input("entrer un décor de la tarte (2caractères): ")
while len(de) != 2 :
    de = input("entrer un décor d'arrière plan (2caractères): ")

for i in range(len(dn)):
    refrain = "% "+dn[i]+" %"+(len(dn)-i)*de+"|"
    if i == 7 :
        corp = 2*sy + "   Happy Birthday   " + 2*sy
    elif i == 8 :
        corp = 3*sy
        gap = (i*4)-((len(corp)*2)+len(nom))
        if gap != 0 :
            nom = ((gap//2)*" ") + nom + ((gap-(gap//2))*" ")
        corp = corp + nom + corp
    else :
        corp = i*2*sy
    ligne= refrain + corp + refrain[::-1] 
    print(ligne)