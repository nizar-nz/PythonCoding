from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def play():
    bi = windows.le_inf.text()
    bs = windows.le_sup.text()
    mess = "vérifier les nombres saisie! (numériques, 0 <= borne inf < born sup <= 10000)"
    if bi.isdigit() and bs.isdigit() and 0 <= int(bi) < int (bs) <= 10000:
        mess = ""
        for x in range(int(bi),int(bs)+1):
            if premier(x) and symetrique(x)!=-1 and premier(symetrique(x)):
                mess = str(x) + " | " + mess
        if mess == "" :
            mess = "pas de nombres doublement premier dans cet intervalle!"
    windows.lbl_res.setText(mess)            

def premier(n):
    i=n//2
    while i > 1 and n % i !=0 :
        i = i - 1
    return i == 1

def symetrique(n):
    s = str(n)         #sn=s[::-1]
    sn = ""
    for i in range(len(s)):
        sn = s[i]+sn 
    if n != int(sn):
        return int(sn)
    return -1

app = QApplication([])
windows = loadUi ("NbrDoubPremier.ui")
windows.show()
windows.b_cher.clicked.connect ( play )

app.exec_()