from random import randint
monDict=[]
taille=0
maSource = open("5000_wordlist_french_mv.csv",'r')
for i in maSource:
    ligne=maSource.readline()
    if len(ligne)>5:
        monDict.append(ligne[:len(ligne)-1])
        taille=taille+1
maSource.close
aDeviner = monDict[randint(0,taille)]
introduction = '''Il s'agit de deviner un mot français choisi au hasard !
vous devez saisir une lettre de l'alphabet;
si elle existe, elle apparaît partout où elle existe dans le mot,
sinon vous perdrez un essai, le nombre d'essais est limité à 8
'''
print(introduction)
mesEssais = "_"*len(aDeviner)
gameover = False
essais=8
while not gameover:
    print(mesEssais)
    devinette=input("entrer une lettre : ")
    while len(devinette)!=1:
        devinette=input("entrer une lettre : ")
    if devinette in aDeviner :
        pos=0
        while aDeviner.find(devinette,pos)!=-1:
            pos= aDeviner.find(devinette,pos)
            mesEssais = mesEssais[:pos]+devinette+mesEssais[pos+1:]
            pos=pos+1
    else :
        essais = essais - 1
        
    if aDeviner == mesEssais or essais == 0 :
        gameover = True
if aDeviner == mesEssais :
    print ("bravo!")
else:
    print("perdu!")