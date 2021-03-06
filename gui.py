# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 529)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 611, 171))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.label.setObjectName("label")
        self.device_list = QtWidgets.QComboBox(self.groupBox)
        self.device_list.setGeometry(QtCore.QRect(120, 50, 160, 31))
        self.device_list.setObjectName("device_list")
        self.device_list.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.label_2.setObjectName("label_2")
        self.scale_factor = QtWidgets.QComboBox(self.groupBox)
        self.scale_factor.setGeometry(QtCore.QRect(120, 110, 101, 31))
        self.scale_factor.setObjectName("scale_factor")
        self.scale_factor.addItem("")
        self.scale_factor.addItem("")
        self.scale_factor.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(310, 50, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(310, 110, 101, 31))
        self.label_4.setObjectName("label_4")
        self.format = QtWidgets.QComboBox(self.groupBox)
        self.format.setGeometry(QtCore.QRect(420, 111, 101, 31))
        self.format.setObjectName("format")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.picturemode = QtWidgets.QRadioButton(self.groupBox)
        self.picturemode.setGeometry(QtCore.QRect(420, 50, 71, 31))
        self.picturemode.setChecked(True)
        self.picturemode.setObjectName("picturemode")
        self.videomode = QtWidgets.QRadioButton(self.groupBox)
        self.videomode.setGeometry(QtCore.QRect(500, 50, 71, 31))
        self.videomode.setObjectName("videomode")
        self.start_button = QtWidgets.QPushButton(Dialog)
        self.start_button.setGeometry(QtCore.QRect(160, 470, 141, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.start_button.setCheckable(True)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.display = QtWidgets.QTextBrowser(Dialog)
        self.display.setGeometry(QtCore.QRect(20, 230, 611, 211))
        self.display.setObjectName("display")
        self.stop_button = QtWidgets.QPushButton(Dialog)
        self.stop_button.setGeometry(QtCore.QRect(350, 470, 141, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setCheckable(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "真实图像超分辨率重建系统 v0.1"))
        self.groupBox.setTitle(_translate("Dialog", "参数设置"))
        self.label.setText(_translate("Dialog", "使用设备："))
        self.device_list.setItemText(0, _translate("Dialog", "CPU"))
        self.label_2.setText(_translate("Dialog", "放大系数："))
        self.scale_factor.setItemText(0, _translate("Dialog", "2"))
        self.scale_factor.setItemText(1, _translate("Dialog", "3"))
        self.scale_factor.setItemText(2, _translate("Dialog", "4"))
        self.label_3.setText(_translate("Dialog", "重建模式："))
        self.label_4.setText(_translate("Dialog", "输出格式："))
        self.format.setItemText(0, _translate("Dialog", "bmp"))
        self.format.setItemText(1, _translate("Dialog", "jpg"))
        self.format.setItemText(2, _translate("Dialog", "png"))
        self.picturemode.setText(_translate("Dialog", "图片"))
        self.videomode.setText(_translate("Dialog", "视频"))
        self.start_button.setText(_translate("Dialog", "开始"))
        self.label_5.setText(_translate("Dialog", "输出："))
        self.stop_button.setText(_translate("Dialog", "中止"))
