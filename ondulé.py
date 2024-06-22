ch = ""
while len(ch) < 3 :
    ch=input("entrer une chaine d'au moin 3 caractères : ")
i=0
while ch[i] == ch[i+2] and i < len(ch)-3 :
    i+=1
if ch[i] != ch[i+2] :
    print(ch," n'est pas ondulante")
else :
    print(ch," est ondulante")