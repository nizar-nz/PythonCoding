print("bonjour! Je suis un specialiste de nutrition")
print("Je vais vous aider à calculer votre IMC")
poid=int(input("Quel est ton poid?"))
taille=float(input("Quel est ta taille?"))
IMC = poid/(taille*taille)
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

