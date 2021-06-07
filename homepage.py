from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("homepage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 390, 361, 141))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(850, 550, 511, 441))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("batman.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(840, 10, 461, 431))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("anime.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 610, 461, 441))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("sticker_vk_zheleznyy_chelovek_040.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(120, 50, 561, 301))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("c32c8f8e033d215c0cab30c0321a2bc6.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(1500, 40, 321, 291))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("update.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(1420, 630, 451, 391))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("webtoon.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(lambda: self.hide_widget())
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "COMIC CHARACTER PORTAL"))
        Form.setWindowIcon(QtGui.QIcon("monster.png"))
        self.pushButton.setText(_translate("Form", "Enter the world of Comic Characters"))
        self.pushButton.setIcon(QtGui.QIcon("monster.png"))
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setFont(QtGui.QFont('Comic Sans', 9))

    def hide_widget(self):
        os.system('python main.py')



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
