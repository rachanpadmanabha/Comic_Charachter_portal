import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qdarkstyle
import os

from mainwindow_ui import Ui_MainWindow
from dialog_ui1 import Ui_Dialog
from dialog_ui2 import Ui_Dialog2
from dialog_ui3 import Ui_Dialog3
from dialog_ui4 import Ui_Dialog4
from dialog_ui5 import Ui_Dialog5


class MyDialog1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class MyDialog2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)


class MyDialog3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)


class MyDialog4(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self)


class MyDialog5(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog5()
        self.ui.setupUi(self)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Menubar()

    def Menubar(self):
        _translate = QCoreApplication.translate
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 25, 26))
        menubar.setObjectName("menubar")
        menuFILE = QMenu(menubar)
        menuFILE.setTitle(_translate("MainWindow", "FILE"))
        actionabout = QAction(self)
        menubar.addAction(actionabout)
        actionabout.setText(_translate("MainWindow", "ABOUT US"))
        # actionabout.triggered.connect()
        actionadmin = QAction(self)
        menubar.addAction(actionadmin)
        actionadmin.setText(_translate("MainWindow", "ADMIN"))
        actionadmin.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        actionadmin.triggered.connect(lambda: os.system("python sign_in.py"))

    def dialogbox1(self):
        self.myDialog1 = MyDialog1()
        self.myDialog1.show()

    def dialogbox2(self):
        self.myDialog2 = MyDialog2()
        self.myDialog2.show()

    def dialogbox3(self):
        self.myDialog3 = MyDialog3()
        self.myDialog3.show()

    def dialogbox4(self):
        self.myDialog4 = MyDialog4()
        self.myDialog4.show()

    def dialogbox5(self):
        self.myDialog5 = MyDialog5()
        self.myDialog5.show()

    def dialogbox6(self):
        os.system('python versus.py')

    def dialogbox7(self):
        os.system('python space_invader.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
