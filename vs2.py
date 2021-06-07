from PyQt5 import QtCore, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
import mysql.connector as mc


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.value_set1 = QBarSet(f"{self.v1}")
        self.value_set2 = QBarSet(f"{self.v2}")

        values, values2 = self.get_data(self.v1, self.v2)
        self.value_set1 << values[0][0] << values[0][1] << values[0][2] << values[0][3] << values[0][4] << values[0][
            5] << \
        values[0][6]
        self.value_set2 << values2[0][0] << values2[0][1] << values2[0][2] << values2[0][3] << values2[0][4] << \
        values2[0][
            5] << values2[0][6]

        self.series = QPercentBarSeries()
        self.series.append(self.value_set1)
        self.series.append(self.value_set2)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle(str(self.v1) + " vs " + str(self.v2))
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.Lengends = ["Intelligence", "Strength", "Speed", "Durability", "Power", "Combat", "Tier"]
        self.axis = QBarCategoryAxis()
        self.axis.append(self.Lengends)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axis, self.series)

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        MainWindow.setCentralWidget(self.chartview)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_data(self, v1, v2):
        query1 = f"""select s.Intelligence, s.Strength, s.Speed, s.Durability, s.Power, s.Combat, s.Tier from stats s,protagonist p where (p.Alias = "{v1}" or p.Name = "{v1}") and s.Protagonist_id = p.Protagonist_id; """
        query2 = f"""select s.Intelligence, s.Strength, s.Speed, s.Durability, s.Power, s.Combat, s.Tier from stats s,antagonist a where (a.Alias = "{v1}" or a.Name = "{v1}") and a.Antagonist_id = s.Antagonist_id; """
        query3 = f"""select s.Intelligence, s.Strength, s.Speed, s.Durability, s.Power, s.Combat, s.Tier from stats s,protagonist p where (p.Alias = "{v2}" or p.Name = "{v2}") and s.Protagonist_id = p.Protagonist_id; """
        query4 = f"""select s.Intelligence, s.Strength, s.Speed, s.Durability, s.Power, s.Combat, s.Tier from stats s,antagonist a where (a.Alias = "{v2}" or a.Name = "{v2}") and s.Antagonist_id = a.Antagonist_id; """
        result1 = []
        result2 = []
        result3 = []
        result4 = []
        try:
            mydb1 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur1 = mydb1.cursor()
            mycur1.execute(query1)
            result1 = mycur1.fetchall()
            print("result1 =", result1)



        except mc.Error as e:
            print(e)

        try:
            mydb2 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur2 = mydb2.cursor()
            mycur2.execute(query2)
            result2 = mycur2.fetchall()
            print("result2 = ", result2)


        except mc.Error as e:
            print(e)

        try:
            mydb1 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur3 = mydb1.cursor()
            mycur3.execute(query3)
            result3 = mycur3.fetchall()
            print("result3 = ", result3)


        except mc.Error as e:
            print(e)

        try:
            mydb1 = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="portal"

            )
            mycur4 = mydb1.cursor()
            mycur4.execute(query4)
            result4 = mycur4.fetchall()
            print("result4 = ", result4)

        except mc.Error as e:
            print(e)

        asd = [[0, 0, 0, 0, 0, 0, 0]]

        if result1 and result3:
            return (result1, result3)
        elif result1 and result4:
            return (result1, result4)
        elif result2 and result3:
            return (result2, result3)
        elif result2 and result4:
            return (result2, result4)
        elif result1 and not (result2 and result3 and result4):
            asd[0][0] = 100 - (result1[0][0])
            asd[0][1] = 100 - (result1[0][1])
            asd[0][2] = 100 - (result1[0][2])
            asd[0][3] = 100 - (result1[0][3])
            asd[0][4] = 100 - (result1[0][4])
            asd[0][5] = 100 - (result1[0][5])
            asd[0][6] = 10 - (result1[0][6])
            print(asd)
            return (result1, asd)
        elif result2 and not (result1 and result3 and result4):
            asd[0][0] = 100 - (result2[0][0])
            asd[0][1] = 100 - (result2[0][1])
            asd[0][2] = 100 - (result2[0][2])
            asd[0][3] = 100 - (result2[0][3])
            asd[0][4] = 100 - (result2[0][4])
            asd[0][5] = 100 - (result2[0][5])
            asd[0][6] = 8 - (result2[0][6])
            return (result2, asd)
        elif result3 and not (result2 and result1 and result4):
            asd[0][0] = 100 - (result3[0][0])
            asd[0][1] = 100 - (result3[0][1])
            asd[0][2] = 100 - (result3[0][2])
            asd[0][3] = 100 - (result3[0][3])
            asd[0][4] = 100 - (result3[0][4])
            asd[0][5] = 100 - (result3[0][5])
            asd[0][6] = 8 - (result3[0][6])
            return (result3, asd)
        elif result4 and not (result2 and result3 and result1):
            asd[0][0] = 100 - (result4[0][0])
            asd[0][1] = 100 - (result4[0][1])
            asd[0][2] = 100 - (result4[0][2])
            asd[0][3] = 100 - (result4[0][3])
            asd[0][4] = 100 - (result4[0][4])
            asd[0][5] = 100 - (result4[0][5])
            asd[0][6] = 8 - (result4[0][6])
            return (result4, asd)
        else:
            return (asd, asd)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VSSSSSS"))

    def passing_variables(self, a, b):
        self.v1 = a
        self.v2 = b
