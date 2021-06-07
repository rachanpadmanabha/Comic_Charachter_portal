from PyQt5 import QtCore, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
import mysql.connector as mc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        value_set1 = QBarSet("Deadshot")
        value_set2 = QBarSet("Batman")

        values, values2 = self.get_data()
        value_set1 << values[0][0] << values[0][1] << values[0][2] << values[0][3] << values[0][4] << values[0][5] << \
        values[0][6]
        value_set2 << values2[0][0] << values2[0][1] << values2[0][2] << values2[0][3] << values2[0][4] << values2[0][
            5] << values2[0][6]

        series = QPercentBarSeries()
        series.append(value_set1)
        series.append(value_set2)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Deadshot V/s Batman")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        Lengends = ["Intelligence", "Strength", "Speed", "Durability", "Power", "Combat", "Tier"]
        axis = QBarCategoryAxis()
        axis.append(Lengends)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        MainWindow.setCentralWidget(chartview)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_data(self):
        query1 = "select intelligence, Strength, Speed, Durability, Power, Combat, Tier from stats where Protagonist_id = 1016;"
        query2 = "select intelligence, Strength, Speed, Durability, Power, Combat, Tier from stats where Protagonist_id = 1001;"
        try:
            mydb1 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur = mydb1.cursor()
            mycur.execute(query1)
            result1 = mycur.fetchall()

        except mc.Error as e:
            print(e)

        try:
            mydb2 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur = mydb2.cursor()
            mycur.execute(query2)
            result2 = mycur.fetchall()
            return (result1, result2)

        except mc.Error as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
