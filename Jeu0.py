def Chance(ch):
    if not (ch.isdigit() and len(ch)==8 and ch[0] in ["2","4",'5','9']):
        msg="Vérifier le numéro de télephone!"
    else:
        msg="Désolé vous n'avez pas gagné."
        s=0
        For i in range (len(ch)) :
            s+=int(ch[i])*i
            if premier(s):
                msg="Félicitations, vous avez gagné."
    return msg