ch = ""
cond = False
while ch =="" or not cond:
    ch = input("entrer une chaine non vide (que des majuscules) : ")
    cond = True
    i=0
    while cond and i < len(ch):
        cond = 'A' <= ch[i] <= 'Z'
        i = i + 1
p=0
for i in range (len(ch)):
    if ch[i]=='A':
        p=p+(i+1)*1
    elif ch[i]=='E':
        p=p+(i+1)*5
    elif ch[i]=='I':
        p=p+(i+1)*9
    elif ch[i]=='O':
        p=p+(i+1)*15
    elif ch[i]=='U':
        p=p+(i+1)*21
    elif ch[i]=='Y':
        p=p+(i+1)*25
print(p)
        