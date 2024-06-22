from random import randint
from numpy import array
#initialisation du tableau T pour modéliser le chemin de l'oie
T = array([int]*35)
for i in range(35):
    T[i]=0
T[2],T[6],T[8],T[9],T[13],T[15],T[18],T[20],T[26],T[27],T[31],=9,1,11,-5,1,-3,5,1,3,1,-14

#position de départ
i , j = 0 , 0
while i < 34 and j < 34:
    input('appuyer sur "Entrer" pour lancer le dés: ')
    tord , mont = randint(1,6) , randint(1,6)
    if i + mont > 34:
        mont = 34 - i
    if j + tord > 34:
        tord = 34 - j
    print("vous: ancienne position: ",i ,"+ dés =",mont,"\t+",T[i + mont],"\t= nouvelle position:",i + mont + T[i + mont])
    i = i + mont + T[i + mont]
    if i < 34:
        print("ordi: ancienne position: ",j ,"+ dés =",tord,"\t+",T[j + tord],"\t= nouvelle position:",j + tord + T[j + tord])
        j = j + tord + T[j + tord]
if i == 34 :
    print("bravo! vous avez gangé")
else:
    print("l'ordinateur à gagné")
    