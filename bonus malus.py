'''
ch=input("donner une chaine de caractere")
while len(ch) == 0 :
    ch=input("donner une chaine de caractere non vide")
    
ch = ""
while len(ch) < 8 or len(ch) > 16 :
    ch=input("donner une chaine de caractere non vide")
'''
   
ch = ""
while not (len(ch) >= 8 and len(ch) <= 16) :
    ch=input("donner une chaine de caractere non vide : ")
i = 0
plsm=0
while i <= len(ch)-1:    
    while not(ord(ch[i])>=97 and ord(ch[i])<=122):
        i = i + 1
        if i > len(ch)-1: break
    Sm=0    
    if i < len(ch): 
        while ord(ch[i])>=97 and ord(ch[i])<=122:
            i=i+1
            Sm=Sm+1
            if i > len(ch)-1: break
    print(Sm)
    if Sm > plsm : plsm = Sm
print ("la plus longue séquence miuscule est : ",plsm) 
