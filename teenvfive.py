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

        value_set1 = QBarSet("Teen Titans")
        value_set2 = QBarSet("Fearsome Five")

        values, values2 = self.get_data()
        value_set1 << (
                    values[0][0] + values[1][0] + values[2][0] + values[3][0] + values[4][0] + values[5][0] + values[6][
                0] + values[7][0]) / 8 \
        << (values[0][1] + values[1][1] + values[2][1] + values[3][1] + values[4][1] + values[5][1] + values[6][1] +
            values[7][1]) / 8 \
        << (values[0][2] + values[1][2] + values[2][2] + values[3][2] + values[4][2] + values[5][2] + values[6][2] +
            values[7][2]) / 8 \
        << (values[0][3] + values[1][3] + values[2][3] + values[3][3] + values[4][3] + values[5][3] + values[6][3] +
            values[7][3]) / 8 \
        << (values[0][4] + values[1][4] + values[2][4] + values[3][4] + values[4][4] + values[5][4] + values[6][4] +
            values[7][4]) / 8 \
        << (values[0][5] + values[1][5] + values[2][5] + values[3][5] + values[4][5] + values[5][5] + values[6][5] +
            values[7][5]) / 8 \
        << (values[0][6] + values[1][6] + values[2][6] + values[3][6] + values[4][6] + values[5][6] + values[6][6] +
            values[7][6]) / 8

        value_set2 << (values2[0][0] + values[1][0] + values[2][0] + values[3][0] + values[4][0]) / 5 \
        << (values2[0][1] + values[1][1] + values[2][1] + values[3][1] + values[4][1]) / 5 \
        << (values2[0][2] + values[1][2] + values[2][2] + values[3][2] + values[4][2]) / 5 \
        << (values2[0][3] + values[1][3] + values[2][3] + values[3][3] + values[4][3]) / 5 \
        << (values2[0][4] + values[1][4] + values[2][4] + values[3][4] + values[4][4]) / 5 \
        << (values2[0][5] + values[1][5] + values[2][5] + values[3][5] + values[4][5]) / 5 \
        << (values2[0][6] + values[1][6] + values[2][6] + values[3][6] + values[4][6]) / 5

        series = QPercentBarSeries()
        series.append(value_set1)
        series.append(value_set2)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Teen Titans V/s Fearsome Five")
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
        query1 = "select stats.intelligence, stats.Strength, stats.Speed, stats.Durability, stats.Power, stats.Combat, stats.Tier from stats inner join Protagonist on stats.Protagonist_id=Protagonist.Protagonist_id where stats.Protagonist_id between 1008 and 1015;"
        query2 = "select stats.intelligence, stats.Strength, stats.Speed, stats.Durability, stats.Power, stats.Combat, stats.Tier from stats inner join Antagonist on stats.Antagonist_id=Antagonist.Antagonist_id where stats.Antagonist_id between 2008 and 2012;"
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
