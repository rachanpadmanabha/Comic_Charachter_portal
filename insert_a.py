from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from error_invalid_details import Ui_Dialog4
from error_invalid_details import Ui_Dialog2
from PyQt5.QtWidgets import QDialog, QWidget


class error_box(QDialog):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_Dialog4()
        self.ui1.setupUi(self)


class error_box2(QDialog):
    def __init__(self):
        super().__init__()
        self.ui1 = Ui_Dialog2()
        self.ui1.setupUi(self)


class Ui_MainWindow(object):
    def InsertData1(self):
        ant_id = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        pub_id = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        team_id = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]
        pr_id = [self.tableWidget.item(row, 3).text() for row in range(self.tableWidget.rowCount())]
        name = [self.tableWidget.item(row, 4).text() for row in range(self.tableWidget.rowCount())]
        alias = [self.tableWidget.item(row, 5).text() for row in range(self.tableWidget.rowCount())]
        appearance = [self.tableWidget.item(row, 6).text() for row in range(self.tableWidget.rowCount())]

        print(ant_id[0], pub_id[0], team_id[0], pr_id[0], name[0], alias[0], appearance[0])
        query1 = f"INSERT INTO antagonist (Antagonist_id, Publisher_id, Team_id,Protagonist_id, Name, Alias, Appearance) VALUES ({int(ant_id[0])}, {int(pub_id[0])}, {int(team_id[0])}, {int(pr_id[0])}, '{name[0]}', '{alias[0]}', {int(appearance[0])});"

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )

            mycursor1 = mydb.cursor()

            mycursor1.execute(query1)
            mydb.commit()
            self.err1 = error_box()
            self.err1.show()

        except mc.Error as e:
            print(e)
            self.err = error_box2()
            self.err.show()

    def InsertData2(self):
        ant_id1 = [self.tableWidget_2.item(row, 0).text() for row in range(self.tableWidget_2.rowCount())]
        intelligence = [self.tableWidget_2.item(row, 1).text() for row in range(self.tableWidget_2.rowCount())]
        strength = [self.tableWidget_2.item(row, 2).text() for row in range(self.tableWidget_2.rowCount())]
        speed = [self.tableWidget_2.item(row, 3).text() for row in range(self.tableWidget_2.rowCount())]
        durability = [self.tableWidget_2.item(row, 4).text() for row in range(self.tableWidget_2.rowCount())]
        power = [self.tableWidget_2.item(row, 5).text() for row in range(self.tableWidget_2.rowCount())]
        combat = [self.tableWidget_2.item(row, 6).text() for row in range(self.tableWidget_2.rowCount())]
        tier = [self.tableWidget_2.item(row, 7).text() for row in range(self.tableWidget_2.rowCount())]
        pr_id1 = 1067
        query2 = f"INSERT INTO stats (Protagonist_id, Antagonist_id, Intelligence, Strength, Speed, Durability, Power, Combat, Tier) VALUES ({pr_id1}, {int(ant_id1[0])},  {int(intelligence[0])}, {int(strength[0])}, '{int(speed[0])}', '{int(durability[0])}', {int(power[0])}, {int(combat[0])}, '{int(tier[0])}');"
        try:
            mydb1 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycursor2 = mydb1.cursor()
            mycursor2.execute(query2)
            mydb1.commit()
            self.err1 = error_box()
            self.err1.show()

        except mc.Error as e:
            print(e)
            self.err = error_box2()
            self.err.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 520)
        MainWindow.setFixedSize(1000, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 250, 960, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(12, 12, 911, 221))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.InsertData1)
        self.pushButton_2.clicked.connect(self.InsertData2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        MainWindow.setWindowIcon(QtGui.QIcon("adminicon.jpg"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Antagonist_id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Intelligence"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Strength"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Speed"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Durability"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Power"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Combat"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Tier"))
        self.pushButton_2.setText(_translate("MainWindow", "Insert"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Antagonist_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Publisher_id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Team_id"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protagonist_id"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Alias"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Appearance"))
        self.pushButton.setText(_translate("MainWindow", "Insert"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
