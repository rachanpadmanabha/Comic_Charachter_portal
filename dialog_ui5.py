from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as connector
import sys
from PyQt5.QtGui import QFont


class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(1920, 1080)
        self.label = QtWidgets.QLabel(Dialog5)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("dcc.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog5)
        self.label2.setGeometry(QtCore.QRect(860, 130, 200, 50))
        self.label2.setText("Alliance Table")
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label2.setStyleSheet("QLabel {background-color: transparent;}")

        self.label2.setFont(QFont('Comic Sans MS', 12))

        self.tableWidget = QtWidgets.QTableWidget(Dialog5)
        self.tableWidget.setStyleSheet("""QTableWidget {background-color: transparent;}"
              "QHeaderView::section {background-color: transparent;}"
              "QHeaderView {background-color: transparent;}"
              "QTableCornerButton::section {background-color: transparent;}""")
        self.tableWidget.setGeometry(QtCore.QRect(570, 190, 780, 700))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item1)

        item2 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item2)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 300)

        self.loaddata()

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle("team")
        Dialog5.setWindowIcon(QtGui.QIcon("team.png"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog5", "Created_by"))
        item.setFont(QFont('Times', 16))

        item1 = self.tableWidget.horizontalHeaderItem(1)
        item1.setText(_translate("Dialog5", "Name"))
        item1.setFont(QFont('Times', 16))

        item2 = self.tableWidget.horizontalHeaderItem(2)
        item2.setText(_translate("Dialog5", "No_of_charhters"))
        item2.setFont(QFont('Times', 16))

        self.tableWidget.setFont(QFont('Comic Sans MS', 12))

        self

    def loaddata(self):
        try:
            db = connector.connect(host='localhost', port='3306', user='root', password='', database='portal')
            print("Sucessful")

        except connector.Error as e:
            sys.exit(1)
        cur = db.cursor()
        sqlstr = 'SELECT * from ALLIANCE;'

        table_row = 0
        cur.execute(sqlstr)
        results = cur.fetchall()
        self.tableWidget.setRowCount(25)
        for row in results:
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))

            table_row += 1
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
