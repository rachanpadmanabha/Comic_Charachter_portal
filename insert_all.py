from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from error_invalid_details import Ui_Dialog4, Ui_Dialog2
import mysql.connector as mc


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
        team_id = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        created = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        name = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]
        no_of_chrachters = [self.tableWidget.item(row, 3).text() for row in range(self.tableWidget.rowCount())]

        # print(pr_id[0], pub_id[0], team_id[0], name[0], alias[0], appearance[0], creator[0])
        query1 = f"INSERT INTO alliance (Team_id, Name, Created, No_Of_Characters) VALUES ({int(team_id[0])}, '{created[0]}', '{name[0]}', {int(no_of_chrachters[0])});"

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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 280)
        MainWindow.setFixedSize(627, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(13, 13, 571, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
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
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.InsertData1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        MainWindow.setWindowIcon(QtGui.QIcon("adminicon.jpg"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Created by"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "No_of_Charachters"))
        self.pushButton.setText(_translate("MainWindow", "Insert"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
