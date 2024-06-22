ch=""
while ch=="":
    ch=input("donner une chaine de caractère non vide")
p=0    
for i in range (len(ch)):
    p=p+ord(ch[i])*(i+1)
print("le poids de",ch,"est",p)    
