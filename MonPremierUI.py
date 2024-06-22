from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

# votre code ici
def nombre():
    n=int(windows.txt.text())
    s=0
    for i in range (1,n+1):
        if n%i==0 :
            s=s+1
    windows.lbl_res.setText(str(s))

app = QApplication([])
windows = loadUi ("interface.ui")
windows.show()
#code
windows.Butt1.clicked.connect (nombre)

app.exec_()