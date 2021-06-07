from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 26))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        MainWindow.setMenuBar(self.menubar)
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        # self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ccropped-1920-1080-232866.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(200, 200, 400, 100))
        self.pushButton1.setStyleSheet("""QPushButton {background-color:black;
                                                        border-style: outset;
                                                        border-width: 2px;
                                                        border-radius: 35px;
                                                        border-color: white;
                                                        padding: 4px;}""")
        self.pushButton1.setIcon(QtGui.QIcon("marvel.png"))
        self.pushButton1.setIconSize(QtCore.QSize(100, 100))
        self.pushButton1.setToolTip("For Marvel Characters...")
        self.pushButton1.setObjectName("pushButton1")
        # self.verticalLayout.addWidget(self.pushButton1)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 600, 400, 100))
        self.pushButton2.setIcon(QtGui.QIcon("826335.png"))
        self.pushButton2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton2.setToolTip("For DC Characters...")
        self.pushButton2.setObjectName("pushButton2")
        # self.verticalLayout.addWidget(self.pushButton2)
        self.pushButton2.setStyleSheet("""QPushButton {background-color:black;
                                                                border-style: outset;
                                                                border-width: 2px;
                                                                border-radius: 35px;
                                                                border-color: white;
                                                                padding: 4px;}""")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(1200, 200, 400, 100))
        self.pushButton3.setIcon(QtGui.QIcon("anime.png"))
        self.pushButton3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton3.setToolTip("For Anime Characters...")
        self.pushButton3.setObjectName("pushButton3")
        # self.verticalLayout.addWidget(self.pushButton3)
        self.pushButton3.setStyleSheet("""QPushButton {background-color:black;
                                                                        border-style: outset;
                                                                        border-width: 2px;
                                                                        border-radius: 35px;
                                                                        border-color: white;
                                                                        padding: 4px;}""")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(1200, 600, 400, 100))
        self.pushButton4.setIcon(QtGui.QIcon("webtoon.png"))
        self.pushButton4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton4.setToolTip("For WebToon Characters...")
        self.pushButton4.setObjectName("pushButton4")
        # self.verticalLayout.addWidget(self.pushButton4)
        self.pushButton4.setStyleSheet("""QPushButton {background-color:black;
                                                                                border-style: outset;
                                                                                border-width: 2px;
                                                                                border-radius: 35px;
                                                                                border-color: white;
                                                                                padding: 4px;}""")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(720, 600, 400, 100))
        self.pushButton5.setIcon(QtGui.QIcon("team-icon.png"))
        self.pushButton5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton5.setToolTip("For Alliances of charachters...")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("""QPushButton {background-color:black;
                                                                                border-style: outset;
                                                                                border-width: 2px;
                                                                                border-radius: 35px;
                                                                                border-color: white;
                                                                                padding: 4px;}""")

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(720, 200, 400, 100))
        self.pushButton6.setIcon(QtGui.QIcon("vs-button-742274.png"))
        self.pushButton6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton6.setToolTip("Charachter vs any Charachter...")
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("""QPushButton {background-color:black;
                                                                                border-style: outset;
                                                                                border-width: 2px;
                                                                                border-radius: 35px;
                                                                                border-color: white;
                                                                                padding: 4px;}""")

        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(1820, 930, 100, 100))
        self.pushButton7.setIcon(QtGui.QIcon("multimedia_stick_game_play_controller-512.png"))
        self.pushButton7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton7.setToolTip("Boredom hit hard.....play game")
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setStyleSheet("""QPushButton {background-color:;
                                                                                border-style: outset;
                                                                                border-width: 2px;
                                                                                border-radius: 35px;
                                                                                border-color: white;
                                                                                padding: 4px;}""")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton1.clicked.connect(MainWindow.dialogbox1)
        self.pushButton2.clicked.connect(MainWindow.dialogbox2)
        self.pushButton3.clicked.connect(MainWindow.dialogbox3)
        self.pushButton4.clicked.connect(MainWindow.dialogbox4)
        self.pushButton5.clicked.connect(MainWindow.dialogbox5)
        self.pushButton6.clicked.connect(MainWindow.dialogbox6)
        self.pushButton7.clicked.connect(MainWindow.dialogbox7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comic Character Portal"))
        MainWindow.setWindowIcon(QtGui.QIcon("home.png"))

        self.pushButton1.setText(_translate("MainWindow", "Marvel"))
        self.pushButton2.setText(_translate("MainWindow", "DC"))
        self.pushButton3.setText(_translate("MainWindow", "Anime"))
        self.pushButton4.setText(_translate("MainWindow", "Manhwa"))
        self.pushButton5.setText(_translate("MainWindow", "Teams"))
        self.pushButton6.setText(_translate("MainWindow", "Versus"))
        self.pushButton1.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton5.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton2.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton3.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton4.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton6.setFont(QtGui.QFont('Comic Sans', 15))
        self.pushButton7.setFont(QtGui.QFont('Comic Sans', 15))
