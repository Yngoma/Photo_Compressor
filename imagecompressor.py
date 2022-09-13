# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagecompressor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import PIL
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(QWidget):
     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 402)
        MainWindow.setStyleSheet("background-color: rgb(119, 118, 123);\n"
                                "QlineEdit{\n"
                                "border: 2px dolid gray;\n"
                                "border-radius: 30px;\n"
                                "               }\n"
                                "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
                                        "background-color: rgb(119, 118, 123);")
        self.centralwidget.setObjectName("centralwidget")
        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(440, 310, 83, 25))
        self.Exit_Button.setStyleSheet("background-color: rgba(251, 184, 108, 0);")
        self.Exit_Button.setObjectName("Exit_Button")
        self.Exit_Button.clicked.connect(self.button_clicked)
        self.choose_image = QtWidgets.QPushButton(self.centralwidget)
        self.choose_image.setGeometry(QtCore.QRect(240, 210, 101, 25))
        self.choose_image.setStyleSheet("background-color: rgba(251, 184, 108, 0);")
        self.choose_image.setObjectName("choose_image")
        self.choose_image.clicked.connect(self.openFileNameDialog)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 251, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 201, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 140, 62, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 180, 51, 17))
        self.label_4.setObjectName("label_4")
        self.Saveimage = QtWidgets.QPushButton(self.centralwidget)
        self.Saveimage.setGeometry(QtCore.QRect(230, 250, 121, 25))
        self.Saveimage.setStyleSheet("background-color: rgba(251, 184, 108, 0);")
        self.Saveimage.setObjectName("Saveimage")
        self.Saveimage.clicked.connect(self.SaveImage)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 320, 62, 17))
        self.label_5.setObjectName("label_5")
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(220, 320, 211, 17))
        self.Status.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Status.setText("")
        self.Status.setObjectName("Status")
        self.Quality = QtWidgets.QSpinBox(self.centralwidget)
        self.Quality.setGeometry(QtCore.QRect(240, 170, 45, 26))
        self.Quality.setMaximum(80)
        self.Quality.setSingleStep(5)
        self.Quality.setObjectName("Quality")
        self.compressedlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.compressedlineEdit.setGeometry(QtCore.QRect(230, 90, 113, 25))
        self.compressedlineEdit.setObjectName("compressedlineEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 130, 191, 21))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.TrueB = QtWidgets.QRadioButton(self.groupBox)
        self.TrueB.setGeometry(QtCore.QRect(10, 0, 51, 23))
        self.TrueB.setObjectName("TrueB")
        self.FalseB = QtWidgets.QRadioButton(self.groupBox)
        self.FalseB.setGeometry(QtCore.QRect(80, 0, 106, 23))
        self.FalseB.setObjectName("FalseB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global _translate
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhotoCompressorApp"))
        self.Exit_Button.setText(_translate("MainWindow", "Exit"))
        self.choose_image.setText(_translate("MainWindow", "Choose Image"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Image Compressor</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Compressed Image file Name"))
        self.label_3.setText(_translate("MainWindow", "Optimize"))
        self.label_4.setText(_translate("MainWindow", "Quality"))
        self.Saveimage.setText(_translate("MainWindow", "Save Image"))
        self.label_5.setText(_translate("MainWindow", "Status :"))
        self.TrueB.setText(_translate("MainWindow", "True"))
        self.FalseB.setText(_translate("MainWindow", "False"))
        
    def button_clicked(self):
	    sys.exit(app.exec_())
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_loc = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;ImageFiles (*.jpg)", options=options)
        global img 
        img = Image.open(file_loc[0]) 
        
    def SaveImage(self):
        name = self.compressedlineEdit.text()
        if self.TrueB.isChecked():
            optimize = True
        elif self.FalseB.isChecked():
            optimize = False
       
        quality = self.Quality.value()
        img.save( str(name)+".jpg", "JPEG", optimize = optimize, quality = quality)
        self.Status.setText(_translate("MainWindow", "Image is Compressed"))
        print("Image is Compressed")
        

if __name__ == "__main__": 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())