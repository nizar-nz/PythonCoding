from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Premier(N): # N > 1
    i = N // 2
    while N % i != 0 :
        i = i - 1
    return i==1

def SemiPremier(N):
    for i in range (2, (N // 2) + 1):
        if N % i == 0 and Premier(i) and Premier(N // i):
            return True
    return False        

def Play():
    msg="Veuillez introduire un nombre > 2"
    ch = windows.le_nbre.text()
    if ch.isdigit() and int(ch) > 2 :
        N = int(ch)
        if SemiPremier(N) :
            msg=ch + " est semi-premier"
        else:
            msg=ch + " n'est pas semi-premier"
    windows.lbl_res.setText(msg)

app = QApplication([])
windows = loadUi ("InterfaceSemiPremier.ui")
windows.show()
windows.btn_verif.clicked.connect ( Play )

app.exec_()