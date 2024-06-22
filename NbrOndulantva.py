from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def play():
    mess = " veuillez Introduire un nombre >= 100 "
    ch = windows.le_e.text()
    if ch.isdigit() and (int(ch) >= 100):
        N = int(ch)
        if Ondulant(N):
            mess=ch+" est ondulant "
        else:
            mess=ch+" n'est pas ondulant "
    windows.lbl_res.setText(mess)

def Ondulant(N):
    ch=str(N)
    a=ch[0]
    b=ch[1]
    if a==b:
        return False
    i=2
    while i < len(ch) and (ch[i]==ch[i-2])   :
        i=i+1
    return i == len(ch)
app = QApplication([])
windows = loadUi ("C:/bac2023/InterfaceOndulantva.ui")
windows.show()
windows.bt_verif.clicked.connect ( play )

app.exec_()