from random import randint
print("Bonjour!Je suis un spécialiste de nutrition,")
print("Je vais vous aider à calculer votre IMC")
poid = randint(50,150)
taille = randint(70,220)/100
IMC = poid/(taille*taille)
print(poid,taille)
if IMC <= 18.5 :
    print("IMC:" +str (IMC) + "=> maigreur")
elif IMC <= 24.9 :
    print(" IMC:" +str (IMC) + "=> Normal")
elif IMC <= 29.9 :
    print(" IMC:" +str (IMC) + "=> surpoids")
elif IMC <= 40 :
    print(" IMC:" +str (IMC) + "=> obésité")
else  :
    print(" IMC:" +str (IMC) + "=> obésité morbide")
