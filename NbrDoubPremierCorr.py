from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def play():
    msg="vérifier les nombres saisie! (numériques, 0 <= borne inf < born sup <= 10000)"
    bi = windows.le_inf.text()
    bs = windows.le_sup.text()
def Symetrique(N):
    pass
def Premier(N):
    pass
app = QApplication([])
windows = loadUi ("NbrDoubPremier.ui")
windows.show()
windows.b_cher.clicked.connect ( play )

app.exec_()