print("bonjour je suis un specialiste de nutrition")
print (" je peux vous aider a calculer votre IMC")
poid = float (input(" quel est ton poid (kg)?"))
taille = float (input(" quel est ta taille (m)?"))
IMC = poid / (taille*taille)
if IMC <= 18.5 :
    print ("IMC:" +str(IMC) +" =>maigreur")
elif IMC <= 24.9 :
    print ("IMC:" , IMC ,"=> normal")
elif IMC <= 29.9 :
    print ("IMC:" , IMC ,"=> surpoid")
elif IMC <= 40 :
    print ("IMC:" , IMC ,"=> obesite")
else :
    print ("IMC:" , IMC ,"=> obesite morbide")
