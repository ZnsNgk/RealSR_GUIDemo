from PyQt5 import QtWidgets, QtCore
from control import ControlBoard
import os


class mywindow(QtWidgets.QWidget, ControlBoard):
    def  __init__ (self):
        super(mywindow, self).__init__()
    
def check_folder():
    if not os.path.exists("./input"):
        os.mkdir("./input")
    if not os.path.exists("./output"):
        os.mkdir("./output")
    if not os.path.exists("./temp"):
        os.mkdir("./temp")

if __name__=="__main__":
    import sys
    check_folder()
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())
