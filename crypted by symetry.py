def crypted(ch) :
    if 65 <= ord(ch) <= 90:
        return chr((90-(ord(ch)-65)))
    if 97 <= ord(ch) <= 122:
        return chr((122-(ord(ch)-97)))
    if 48 <= ord(ch) <= 57 :
        return chr((57-(ord(ch)-48)))
    else :
        return(ch)
        
txt, res = "", ""
while txt == "" :
    txt = input("entrer votre message ici :")
for i in txt:
    res = res + crypted(i)
print (res)