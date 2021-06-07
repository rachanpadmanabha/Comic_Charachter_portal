from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import qdarkstyle
from vs2 import Ui_MainWindow1
from PyQt5.QtGui import QFont


class MyDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow1()
        self.ui.passing_variables(var1, var2)
        self.ui.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 150, 250, 75))
        self.pushButton.setIcon(QtGui.QIcon("dc.png"))
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setFlat(False)
        self.pushButton.setStyleSheet("""QPushButton {background-color:black;
                                                        border-style: outset;
                                                        border-width: 2px;                                                                
                                                        border-radius: 40px;
                                                        border-color: white;
                                                        padding: 4px;}""")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 275, 250, 75))
        self.pushButton_2.setIcon(QtGui.QIcon("dc.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 400, 250, 75))
        self.pushButton_3.setIcon(QtGui.QIcon("dc.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 525, 250, 75))
        self.pushButton_4.setIcon(QtGui.QIcon("marvel.png"))
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 650, 250, 75))
        self.pushButton_5.setIcon(QtGui.QIcon("marvel.png"))
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 775, 250, 75))
        self.pushButton_6.setIcon(QtGui.QIcon("anime.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 900, 265, 75))
        self.pushButton_7.setIcon(QtGui.QIcon("anime.png"))
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 150, 250, 75))
        self.pushButton_8.setIcon(QtGui.QIcon("anime.png"))
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_9.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_9.setGeometry(QtCore.QRect(730, 150, 250, 90))
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(730, 400, 250, 90))
        self.pushButton_11.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_11.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(730, 275, 250, 90))
        self.pushButton_10.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_10.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(730, 650, 250, 90))
        self.pushButton_13.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(720, 775, 250, 90))
        self.pushButton_14.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_14.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_14.setFlat(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(720, 900, 250, 90))
        self.pushButton_15.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_15.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(730, 525, 250, 90))
        self.pushButton_12.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(1000, 150, 250, 90))
        self.pushButton_16.setIcon(QtGui.QIcon("vs11.png"))
        self.pushButton_16.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;                                                                
                                                                border-radius: 40px;
                                                                border-color: white;
                                                                padding: 4px;}""")

        self.pushButton_17 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_17.setGeometry(QtCore.QRect(1470, 805, 281, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)

        font1 = QtGui.QFont()
        font1.setFamily("Comic Sans MS")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(60)
        self.pushButton_16.setFont(font1)
        self.pushButton_15.setFont(font1)
        self.pushButton_14.setFont(font1)
        self.pushButton_13.setFont(font1)
        self.pushButton_12.setFont(font1)
        self.pushButton_11.setFont(font1)
        self.pushButton_10.setFont(font1)
        self.pushButton_9.setFont(font1)
        self.pushButton_8.setFont(font1)
        self.pushButton_7.setFont(font1)
        self.pushButton_6.setFont(font1)
        self.pushButton_5.setFont(font1)
        self.pushButton_2.setFont(font1)
        self.pushButton_4.setFont(font1)
        self.pushButton_3.setFont(font1)
        self.pushButton.setFont(font1)



        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(710, 150, 2, 352))
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1310, 150, 8, 325))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("versus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        """self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 50, 341, 91))
        self.textBrowser.setObjectName("textBrowser")"""
        self.label.raise_()

        self.label4 = QtWidgets.QLabel(MainWindow)
        self.label4.setGeometry(QtCore.QRect(205, 100, 200, 50))
        self.label4.setText("SAME PUBLISHER")
        self.label4.setScaledContents(True)
        self.label4.setObjectName("label4")
        self.label4.setStyleSheet("QLabel {background-color: transparent;}")
        self.label4.setFont(QFont('Comic Sans MS', 12))

        self.label5 = QtWidgets.QLabel(MainWindow)
        self.label5.setGeometry(QtCore.QRect(850, 100, 200, 50))
        self.label5.setText("TEAM VS TEAM")
        self.label5.setScaledContents(True)
        self.label5.setObjectName("label5")
        self.label5.setStyleSheet("QLabel {background-color: transparent;}")
        self.label5.setFont(QFont('Comic Sans MS', 12))

        self.label6 = QtWidgets.QLabel(MainWindow)
        self.label6.setGeometry(QtCore.QRect(1440, 700, 350, 50))
        self.label6.setText("ANY CHARACTER COMPARISON")
        self.label6.setScaledContents(True)
        self.label6.setObjectName("label6")
        self.label6.setStyleSheet("QLabel {background-color: ;}")
        self.label6.setFont(QFont('Comic Sans MS', 12))

        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_11.raise_()
        self.pushButton_10.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_12.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.line.raise_()
        self.line_2.raise_()
        # self.textBrowser.raise_()

        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(1340, 750, 550, 51))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit2.setGeometry(QtCore.QRect(1340, 850, 550, 51))
        self.lineEdit2.setObjectName("lineEdit2")

        self.label_2 = QtWidgets.QLabel(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow.setWindowOpacity(0.85)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: os.system("python batvbane.py"))
        self.pushButton_2.clicked.connect(lambda: os.system("python robinvpsimon.py"))
        self.pushButton_3.clicked.connect(lambda: os.system("python Deadshotvbatman.py"))
        self.pushButton_4.clicked.connect(lambda: os.system("python captainvthanos.py"))
        self.pushButton_5.clicked.connect(lambda: os.system("python spidervvenom.py"))
        self.pushButton_6.clicked.connect(lambda: os.system("python rockvkokushibo.py"))
        self.pushButton_7.clicked.connect(lambda: os.system("python 8thvstark.py"))
        self.pushButton_8.clicked.connect(lambda: os.system("python luffyvakainu.py"))
        self.pushButton_9.clicked.connect(lambda: os.system("python justicevdoom.py"))
        self.pushButton_10.clicked.connect(lambda: os.system("python teenvfive.py"))
        self.pushButton_11.clicked.connect(lambda: os.system("python avengervorder.py"))
        self.pushButton_12.clicked.connect(lambda: os.system("python defendervcarnage.py"))
        self.pushButton_13.clicked.connect(lambda: os.system("python pillarsvupper.py"))
        self.pushButton_14.clicked.connect(lambda: os.system("python goteivespada.py"))
        self.pushButton_15.clicked.connect(lambda: os.system("python yonkovadmiral.py"))
        self.pushButton_16.clicked.connect(lambda: os.system("python fugvjahad.py"))
        self.pushButton_17.clicked.connect(lambda: self.vs2())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Versus"))
        MainWindow.setWindowIcon(QtGui.QIcon("vs1.png"))
        self.pushButton.setText(_translate("MainWindow", "Batman V/s Bane"))
        self.pushButton_2.setText(_translate("MainWindow", "Robin V/s Psimon"))
        self.pushButton_3.setText(_translate("MainWindow", "Deadshot V/s Batman"))
        self.pushButton_4.setText(_translate("MainWindow", "Captain America V/s Thanos"))
        self.pushButton_5.setText(_translate("MainWindow", "Spider-man V/s Venom"))
        self.pushButton_6.setText(_translate("MainWindow", "Rock Pillar V/s Kokushibo"))
        self.pushButton_7.setText(_translate("MainWindow", "8th division Captiain V/s Coyote Stark"))
        self.pushButton_8.setText(_translate("MainWindow", "Luffy V/s Akainu"))
        self.pushButton_9.setText(_translate("MainWindow", "Justice League V/s Legion of Doom"))
        self.pushButton_11.setText(_translate("MainWindow", "Avengers V/s Black Order"))
        self.pushButton_10.setText(_translate("MainWindow", "Teen Titans V/s Fearsome Five"))
        self.pushButton_13.setText(_translate("MainWindow", "The Pillars V/s Upper Moon"))
        self.pushButton_14.setText(_translate("MainWindow", "Gotei 13 V/s Espada"))
        self.pushButton_15.setText(_translate("MainWindow", "Yonko V/s Navy Admirals"))
        self.pushButton_12.setText(_translate("MainWindow", "Defenders V/s Carnage Family"))
        self.pushButton_16.setText(_translate("MainWindow", "FUG Slayers V/s Jahad\'s Army"))
        self.pushButton_17.setText(_translate("MainWindow", "VS"))



    def vs2(self):
        global var1
        global var2
        var1 = self.lineEdit.text()
        var2 = self.lineEdit2.text()
        print(var1)
        print(var2)
        self.myDialog = MyDialog()
        self.myDialog.show()


if __name__ == "__main__":
    import sys, os

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
