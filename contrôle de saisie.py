''' écrire un programme python qui permet de :
saisir une chaîne constituée uniquement de lettres
alpabétique : "a".."z" et "A".."Z" '''
ch=""
i=-1
while i < len(ch) or ch == "":
    ch = input("entrer une chaine de lettres alpabétique : ")
    i = 0
    while i < len(ch) and (("A" <= ch[i] <= "Z") or ("a" <= ch[i] <= "z")) :
        i = i + 1
print("valide")
    
    