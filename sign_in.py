from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import mysql.connector as connector
from error_invalid_details import Ui_Dialog1
from error_invalid_details import Ui_Dialog2
import os


class error_box(QDialog):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_Dialog1()
        self.ui1.setupUi(self)


class error_box2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_Dialog2()
        self.ui2.setupUi(self)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ysFxGz.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(1462, 977, 371, 71))
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(1340, 750, 551, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(1200, 750, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(1200, 810, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(1340, 810, 551, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1402, 887, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.buttonBox.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()

        self.pushButton.clicked.connect(self.login)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Admin Page"))
        Form.setWindowIcon(QtGui.QIcon("adminicon.jpg"))
        self.label_2.setText(_translate("Form", "admin_id"))
        self.label_3.setText(_translate("Form", "password"))
        self.pushButton.setText(_translate("Form", "LOGIN"))

    def login(self):
        global email
        global password
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:

            mydb = connector.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )

            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT admin_id,password from admin where admin_id like '" + email + "'and password like '" + password + "'")
            result = mycursor.fetchone()

            if result == None:
                self.err1 = error_box()
                self.err1.show()



            else:
                os.system(" python admin2.py")



        except connector.Error as e:
            self.err2 = error_box2()
            self.err2.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
0
