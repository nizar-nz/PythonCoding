''' on se propose de réaliser un programme pour crypter nos messages.
le cryptage se fait caractère par caractère de la manière suivante:
si CA est le code ascii du caractère est que CA est pair alors
on le remplace par le caractère qui a le code ascii CA+2 par contre
si CA est impaire alors on le remplace par le caractère qui a le
code ascii CA-2'''
message = input("entrer le message a crypter : " )
mCrypte = ""    # initialisation du message crypter
for i in range (len(message)):   # parcour du message
    if ord(message[i])%2 == 0 :  # code ascii du caractère est pair
        mCrypte = mCrypte + chr(ord(message[i])+2)  # on ajoute caractere (code ascii + 2) 
    else :                       # code ascii du caractère est impair
        mCrypte = mCrypte + chr(ord(message[i])-2)  # on ajoute caractere (code ascii - 2)
print(mCrypte)
                                   