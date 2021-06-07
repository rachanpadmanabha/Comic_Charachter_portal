from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector
from PyQt5.QtGui import QFont
import sys


class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(1920, 1080)
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("animeak.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(Dialog3)
        self.label1.setGeometry(QtCore.QRect(550, 130, 200, 50))
        self.label1.setText("Protagonist Table")
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet("QLabel {background-color: transparent;}")

        self.label2 = QtWidgets.QLabel(Dialog3)
        self.label2.setGeometry(QtCore.QRect(1250, 130, 200, 50))
        self.label2.setText("Antagonist Table")
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label2.setStyleSheet("QLabel {background-color: transparent;}")

        self.label1.setFont(QFont('Comic Sans MS', 12))
        self.label2.setFont(QFont('Comic Sans MS', 12))

        self.tableWidget = QtWidgets.QTableWidget(Dialog3)
        self.tableWidget.setStyleSheet("""QTableWidget {background-color: transparent;}"
                      "QHeaderView::section {background-color: transparent;}"
                      "QHeaderView {background-color: transparent;}"
                      "QTableCornerButton::section {background-color: transparent;}""")
        self.tableWidget.setGeometry(QtCore.QRect(250, 200, 810, 700))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item1)

        item2 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item2)

        item3 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item3)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)

        self.tableWidget1 = QtWidgets.QTableWidget(Dialog3)
        self.tableWidget1.setStyleSheet("""QTableWidget {background-color: transparent;}"
                              "QHeaderView::section {background-color: transparent;}"
                              "QHeaderView {background-color: transparent;}"
                              "QTableCornerButton::section {background-color: yellow;}""")
        self.tableWidget1.setGeometry(QtCore.QRect(1070, 200, 650, 700))
        self.tableWidget1.setObjectName("tableWidget")
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setRowCount(0)

        item10 = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item10)

        item11 = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item11)

        item22 = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item22)

        self.tableWidget1.setColumnWidth(0, 200)
        self.tableWidget1.setColumnWidth(1, 200)
        self.tableWidget1.setColumnWidth(2, 150)
        self.loaddata()

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate

        Dialog3.setWindowTitle("Anime")
        Dialog3.setWindowIcon(QtGui.QIcon("anime.png"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "Name"))
        item.setFont(QFont('Times', 16))

        item1 = self.tableWidget.horizontalHeaderItem(1)
        item1.setText(_translate("Dialog3", "Alias"))
        item1.setFont(QFont('Times', 16))

        item2 = self.tableWidget.horizontalHeaderItem(2)
        item2.setText(_translate("Dialog3", "Appearance"))
        item2.setFont(QFont('Times', 16))

        item3 = self.tableWidget.horizontalHeaderItem(3)
        item3.setText(_translate("Dialog3", "Creator"))
        item3.setFont(QFont('Times', 16))

        item10 = self.tableWidget1.horizontalHeaderItem(0)
        item10.setText(_translate("Dialog3", "Name"))
        item10.setFont(QFont('Times', 16))

        item11 = self.tableWidget1.horizontalHeaderItem(1)
        item11.setText(_translate("Dialog3", "Alias"))
        item11.setFont(QFont('Times', 16))

        item22 = self.tableWidget1.horizontalHeaderItem(2)
        item22.setText(_translate("Dialog3", "Appearance"))
        item22.setFont(QFont('Times', 16))

        self.tableWidget.setFont(QFont('Comic Sans MS', 12))
        self.tableWidget1.setFont(QFont('Comic Sans MS', 12))

    def loaddata(self):
        try:
            db = connector.connect(host='localhost', port='3306', user='root', password='', database='portal')
            print("Sucessful")

        except connector.Error as e:
            sys.exit(1)
        cur = db.cursor()
        sqlstr = 'SELECT * from protagonist where Publisher_id = 3;'

        tablerow = 0
        cur.execute(sqlstr)
        results = cur.fetchall()
        self.tableWidget.setRowCount(25)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[6]))

            tablerow += 1
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        try:
            db1 = connector.connect(host='localhost', port='3306', user='root', password='', database='portal')
            print("Sucessful")

        except connector.Error as e:
            sys.exit(1)
        cur1 = db1.cursor()
        sqlstr1 = 'select * from antagonist where Publisher_id = 3;'
        tablerow1 = 0
        cur1.execute(sqlstr1)
        results1 = cur1.fetchall()
        self.tableWidget1.setRowCount(25)
        for row1 in results1:
            self.tableWidget1.setItem(tablerow1, 0, QtWidgets.QTableWidgetItem(row1[4]))
            self.tableWidget1.setItem(tablerow1, 1, QtWidgets.QTableWidgetItem(row1[5]))
            self.tableWidget1.setItem(tablerow1, 2, QtWidgets.QTableWidgetItem(str(row1[6])))

            tablerow1 += 1
        self.tableWidget1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
