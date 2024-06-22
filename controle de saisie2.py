ch=""
while ch == "":
    ch=input("entrer une chaine : ")
    i=0
    while i < len(ch) and 'A' <= ch[i] <= 'Z' :
        i=i+1
    if not(i==len(ch)):
        ch=""
