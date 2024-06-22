from random import randint
print("bonjour ! je suis un spécialiste de nutrition")
print("je vais vous aider à calculer votre IMC")
poid=randint(50,150)
taille=randint(70,220)/100
IMC=poid/(taille * taille)
if IMC <= 18.5 :
    print("Your IMC is" , IMC , "=> maigreur ",poid,taille)
elif IMC <= 24.9 :
    print("Your IMC is" , IMC , "=> normal",poid,taille)
elif IMC <= 29.9 :
    print("Your IMC is" , IMC , "=> surpoids",poid,taille)
elif IMC <= 40 :
    print("Your IMC is" , IMC , "=> obésité",poid,taille)
else :
    print("Your IMC is" , IMC , "=> obésité mobide",poid,taille)
    
    