print("bonjour ! je suis un spécialiste de nutrition")
print("je vais vous aider à calculer votre IMC")
poid=int(input("Quel est ton poid (kg)"))
taille=float(input("Quel est ta taille (m)"))
IMC=poid/(taille * taille)
if IMC <= 18.5 :
    print("Your IMC is" , IMC , "=> maigreur ")
elif IMC <= 24.9 :
    print("Your IMC is" , IMC , "=> normal")
elif IMC <= 29.9 :
    print("Your IMC is" , IMC , "=> surpoids")
elif IMC <= 40 :
    print("Your IMC is" , IMC , "=> obésité")
else :
    print("Your IMC is" , IMC , "=> obésité mobide")
    
    