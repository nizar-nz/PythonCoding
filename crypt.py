msg =""
while msg=="" :
    msg = input("entrer votre message : ")
resultat = ""
for i in range(len(msg)):
    if (ord(msg[i]) % 2) == 0 :
        resultat = resultat + chr(ord(msg[i])+2)
    else :
        resultat = resultat + chr(ord(msg[i])-2)
print(resultat)
        