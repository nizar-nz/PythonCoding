'''
On connait tous l'arc-en-ciel et ses sept couleurs :
rouge, orange, jaune, vert, bleu, indigo et violet.
écrire un programme python qui permet de demander
les couleurs d'arc en ciel et de vérifier à la fin
s'ils sont correctes , partiellement correctes,
incorrectes et s'ils sont dans l'ordre ou pas'''

c1 = input("entrer la première couleur de l'arc en ciel: ")
c2 = input("entrer la deuxième couleur de l'arc en ciel: ")
c3 = input("entrer la troisième couleur de l'arc en ciel: ")
c4 = input("entrer la quatrième couleur de l'arc en ciel: ")
c5 = input("entrer la cinqième couleur de l'arc en ciel: ")
c6 = input("entrer la sixième couleur de l'arc en ciel: ")
c7 = input("entrer la septième couleur de l'arc en ciel: ")

aec = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
do = True
crc=0
if c1 in aec :
    crc = crc + 1
    if c1 != aec[0]:
        do = False
if c2 in aec : 
    crc = crc + 1
    if c2 != aec[1]:
        do = False
if c3 in aec : 
    crc = crc + 1
    if c3 != aec[2]:
        do = False
if c4 in aec : 
    crc = crc + 1
    if c4 != aec[3]:
        do = False
if c5 in aec : 
    crc = crc + 1
    if c5 != aec[4]:
        do = False
if c6 in aec : 
    crc = crc + 1
    if c6 != aec[5]:
        do = False
if c7 in aec : 
    crc = crc + 1
    if c7 != aec[6]:
        do = False

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
    

