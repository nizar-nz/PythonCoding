from random import randint 
print("bonjour! Je suis un specialiste de nutrition")
print("Je vais vous aider à calculer votre IMC")
poid=randint(40,150)
taille=randint(130,210)/100
IMC = poid/(taille*taille)
print ( poid  ,taille )
if IMC <= 18.5:
    print("IMC: " + str(IMC)+"=> maigreur")
elif IMC <= 24.9:
    print("IMC: " + str(IMC)+"=> normal")
elif IMC <= 29.9:
    print("IMC: " + str(IMC)+"=> surpoids")
elif IMC <= 40:
    print("IMC: " + str(IMC)+"=> obésité")
else:
    print("IMC: " + str(IMC)+"=> obésité morbide")

