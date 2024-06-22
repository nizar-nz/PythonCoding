ch=""
while len(ch) == 0 or ch.find(" ") != -1 :
    ch = input ("entrer une chaine non vide sans esspces : ")
#version 1
#i =0
#while ord(ch(i)) <= ord(ch(i+1)) and i != len(ch)-2 :
#    i = i + 1
#version 2
i =1
while ord(ch[i]) <= ord(ch[i-1]) and i != len(ch)-1 :
    i = i + 1
if ord(ch[i]) <= ord(ch[i-1]) :
    print(ch , " est descendante")
else:
    print(ch , " n'est pas descendante")