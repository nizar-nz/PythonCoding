"""
un mot ascendant est un mot qui va en augmentant, en s'améliorant.
un mot est dit ascendant si chaque caractère possède une position supèrieur ou égal
au caractère qui lui précède dans l'alphabet.
            abcdefghijklmnopqrstuvwxyz
example :
            accent est un mot ascendant
            mort   est un mot ascendant
            films  est un mot ascendant
            BMW    est un mot ascendant
ecrire un programme en Python permetant de saisir une chaîne non vide 
ne contenant pas d'espaces et de vérifier si cette dernière est ascendante ou pas.
"""
ch = ""
while len(ch)==0 and ch.find(" ")!=-1 :
    ch = input("entrer une chaîne non vide ne contenant pas d'espaces : ")
i = 0
while i != len(ch)-2 and ord(ch[i])>=ord(ch[i+1]):
    i=i+1
if i != len(ch)-1 :
    print (ch, "\tn'est pas ascendant")
else :
    print (ch, "\test un mot ascendant")