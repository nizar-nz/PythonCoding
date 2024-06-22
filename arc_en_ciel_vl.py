'''
On connait tous l'arc-en-ciel et ses sept couleurs :
rouge, orange, jaune, vert, bleu, indigo et violet.
écrire un programme python qui permet de demander
les couleurs d'arc en ciel et de vérifier à la fin
s'ils sont correctes , partiellement correctes,
incorrectes et s'ils sont dans l'ordre ou pas'''

aec = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
couleurs = ['noir', 'blanc','gris','maron','rose']
couleurs.extend(aec)
rep = []
for i in range (7):
    coul = ''
    while coul not in couleurs:
        coul = input("entrer la "+str(i+1)+" couleur de l'arc en ciel: ")
    rep.append(coul)

do = True
crc=0
for i in range(7):
    if rep[i] in aec :
        crc = crc + 1
        if rep[i] != aec[i]:
            do = False
print(aec)
print(rep)
if crc == 7 :
    print ("reponses correctes")
elif crc == 0 :
    print ("reponses incorrectes")
else :
    print ("reponses partiellement correctes")
if do :
    print("dans l'ordre")
else :
    print("pas dans l'ordre")