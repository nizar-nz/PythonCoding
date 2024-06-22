from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
# your code here
def nombre():
    n=int(windows.txt.text())
    s=0
    for i in range(1,n+1):
        if n%i==0 :
            s=s+1
    windows.lbl_res.setText(str(s))
app = QApplication([])
windows = loadUi ("interfaceII.ui")
windows.show()
windows.but1.clicked.connect ( nombre )
app.exec_()