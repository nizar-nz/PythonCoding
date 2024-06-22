from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Chance(ch):
    if not (ch.isdigit() and len(ch)==8 and ch[0] in ["2","4","5","9"]):
        msg="vérfier le numéro de teléphone!"
    else:
        msg="désolé,vous n'avez pas gagné."
        s=0
        for i in range (len(ch)):
            s=s+int(ch[i])*i
        if premier(s) :
            msg="Félicitation , vous avez gagné"
        return msg
def premier (n):
    b=2
    p=True
    while b<=n**(1/2) and p:
        if n%b==0:
            p=False
        b+=1
    return p

def Play ():
    num=windows.noumrou.text()
    msg=Chance(num)
    windows.affichage.setText(msg)
    
app = QApplication([])
windows = loadUi ("C:/bac2023/Interface_Jeu.ui")
windows.show()
windows.pushButton.clicked.connect ( Play )


app.exec_()