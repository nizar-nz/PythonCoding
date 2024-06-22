def sym(C):
    return chr(26-((ord(C[0])-65))+64)

for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
    print (sym(c),end="")