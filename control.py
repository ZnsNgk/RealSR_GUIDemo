from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Dialog
from torch.cuda import device_count, get_device_name
import sys
from core import run_demo, set_flag, get_flag

class ControlBoard(Ui_Dialog):
    def  __init__ (self):
        self.setupUi(self)
        self.__check_device()
        self.th = SR_Thread()
        self.th.textWritten.connect(self.outputWritten)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.videomode.toggled.connect(lambda :self.mode_exchange(self.videomode))
        self.picturemode.toggled.connect(lambda :self.mode_exchange(self.picturemode))
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)
    
    def __check_device(self):
        device_num = device_count()
        for i in range(device_num):
            self.device_list.addItem("")
            self.device_list.setItemText(i+1, get_device_name(i))      

    def mode_exchange(self, btn):
        _translate = QtCore.QCoreApplication.translate
        if btn.text()=='图片':
            if btn.isChecked()==True:
                self.format.addItem("")
                self.format.setItemText(0, _translate("Dialog", "bmp"))
                self.format.setItemText(1, _translate("Dialog", "jpg"))
                self.format.setItemText(2, _translate("Dialog", "png"))
            
        if btn.text()=="视频":
            if btn.isChecked() == True:
                self.format.removeItem(2)
                self.format.setItemText(0, _translate("Dialog", "mp4"))
                self.format.setItemText(1, _translate("Dialog", "avi"))
                
    def start(self):
        if self.start_button.isChecked():
            set_flag(False)
            self.display.setText("")
            string = "python demo.py "
            if self.picturemode.isChecked():
                string += "pic "
                mode = "pic"
                format_list = ["bmp", "jpg", "png"]
            elif self.videomode.isChecked():
                string += "vid "
                mode = "vid"
                format_list = ["mp4", "avi"]
            string += "--scale "
            string += str(self.scale_factor.currentIndex() + 2)
            scale = self.scale_factor.currentIndex() + 2
            string += " --device "
            if self.device_list.currentIndex() == 0:
                string += "cpu"
                device = "cpu"
            else:
                string += "cuda:" + str(self.device_list.currentIndex() - 1)
                device = "cuda:" + str(self.device_list.currentIndex() - 1)
            string += " --format "
            string += format_list[self.format.currentIndex()]
            formats = format_list[self.format.currentIndex()]
            print(string)
            arg = args(mode, scale, device, formats)
            self.run(arg)
            self.start_button.toggle()
    
    def stop(self):
        if self.stop_button.isChecked():
            if self.th.isRunning():
                set_flag(True)
                print("中止!")
            self.stop_button.toggle()
    
    def run(self, arg):
        try:
            self.th = SR_Thread(data=arg)
            self.th.start()
        except Exception as e:
            raise e
    
    def outputWritten(self, text):
        cursor = self.display.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.display.setTextCursor(cursor)
        self.display.ensureCursorVisible()

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))

class args():
    def __init__(self, mode, scale, device, formats):
        self.mode = mode
        self.scale = scale
        self.device = device
        self.format = formats

class SR_Thread(QtCore.QThread):
    textWritten = QtCore.pyqtSignal(str)

    def __init__(self,data=None, parent=None):
        super(SR_Thread, self).__init__(parent)
        self.data = data

    def write(self, text):
        self.textWritten.emit(str(text))  # 发射信号

    def run(self):
        sr = run_demo(self.data)
        sr.run()
    