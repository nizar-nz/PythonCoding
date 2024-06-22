def Chance(ch):
    if not (estnum(ch)) and len(ch)==0 and Ch[0] in ["2","4","5","9"]:
        msg=vérfier le numéro de teléphone!
    else:
        msg="désolé,vous n'avez pas gagné."
        s=0
        for i in 0 len(ch):
            s=s+int(ch[i])*i
        if premier(s) :
            msg="Félicitation , vous avez gagné"
        return msg
    pass


