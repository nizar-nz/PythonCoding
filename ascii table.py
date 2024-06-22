n=0
lesChoix = [x+1 for x in range(7,48) if 96%(x+1) ==0]
while n not in lesChoix:
    print("choisi un nombre parmi la liste suivante: ",lesChoix, " ",end='')
    n=int(input ())
ligne = ""
for i in range(32, 32+n):
    ligne = ligne +"| "+str(i)+ "\t"+chr(i)
    for j in range (1,(128//n)+1):
        if (i+n*j) < 128:
            ligne = ligne+" | " + str(i+n*j)+ "\t"+chr(i+n*j)
    print (ligne)
    ligne = ""