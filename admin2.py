from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(700, 60, 480, 640)
        MainWindow.setFixedSize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 640))
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("batman12.jpg"))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 140, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 150, 140, 60))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 500, 140, 60))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: os.system('python insert_p.py'))
        self.pushButton_3.clicked.connect(lambda: os.system('python insert_a.py'))
        self.pushButton_2.clicked.connect(lambda: os.system('python insert_all.py'))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon("adminicon.jpg"))
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "INSERT_P"))
        self.pushButton_2.setText(_translate("MainWindow", "INSERT_AL"))
        self.pushButton_3.setText(_translate("MainWindow", "INSERT_A"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

""""update allian
    set alliance.No_Of_Charachters = alliance.No_Of_Charachters + 1
    where alliance.Team_id = NEW.Team_id;"""
