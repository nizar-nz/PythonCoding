# on se propose de réaliser un programme pour décrypter nos messages.
msg =""    # initialisation du message
while not(msg!="") :  #contrôle de saisie
    msg = input("entrer le message a décrypter : ")
resultat = ""  # initialisation du message décrypter
for i in range(len(msg)):   # parcour caractère par caractère
    if (ord(msg[i]) % 2) == 0 :  # le code ascii du caractère est pair
        resultat = resultat + chr(ord(msg[i])-2)
    else :                       # le code ascii du caractère est impair
        resultat = resultat + chr(ord(msg[i])+2)
print(resultat)