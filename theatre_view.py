from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QSettings
import sys

class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setWindowTitle("Theatre Generator")
        self.setWindowIcon(QtGui.QIcon("kieran's logo.jpg"))
        self.show()
        self.init_UI()
        self.init_menubar()

    def init_UI(self):
        self.setGeometry(200, 200, 1000, 100)
        self.menuLayout = QtWidgets.QHBoxLayout()

        self.lineRow = QtWidgets.QLineEdit(self)
        self.lineRow.setObjectName("Rows")
        self.lineRow.setPlaceholderText("Number of Rows")
        self.menuLayout.addWidget(self.lineRow, 600)

        self.lineCol = QtWidgets.QLineEdit(self)
        self.lineCol.setObjectName("Columns")
        self.lineCol.setPlaceholderText("Number of Columns")
        self.menuLayout.addWidget(self.lineCol, 600)

        self.seatPrice = QtWidgets.QLineEdit(self)
        self.seatPrice.setObjectName("Price")
        self.seatPrice.setPlaceholderText("What is the price of a seat?")
        self.menuLayout.addWidget(self.seatPrice, 700)

        self.generateButton = QtWidgets.QPushButton("generate", self)
        self.menuLayout.addWidget(self.generateButton, 300)

        wid = QtWidgets.QWidget(self)
        self.setMenuWidget(wid)
        wid.setLayout(self.menuLayout)

    def init_menubar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")

        self.menuFile.addAction(self.actionSave)

        translate = QtCore.QCoreApplication.translate
        self.actionSave.setText(translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(translate("MainWindow", "Ctrl+S"))

    def popup_msg(self, message):
        msg = QMessageBox()
        msg.setGeometry(500, 300, 500, 100)
        msg.setWindowTitle("Error")
        msg.setText("Error")
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText(message)
        x = msg.exec_() # executes message box

class SeatsView(MainView):
    def __init__(self):
        super(MainView, self).__init__()
        self.setWindowTitle("Theatre Generator")
        self.setWindowIcon(QtGui.QIcon("kieran's logo.jpg"))
        self.show()
        self.init_UI()
        self.init_menubar()

    def init_UI(self):
        self.gridLayout = QtWidgets.QGridLayout()   # create layout for central widget
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)

    def create_seat_button(self, name, color):
        button = QtWidgets.QPushButton(self)
        button.setText(name)
        button.setMaximumSize(80, 40)
        button.setMinimumSize(30, 20)
        button.setStyleSheet("background-color : " + color)
        # button.clicked.connect(self.seat_button_clicked(button))
        return button

    def seat_button_clicked(self, button):
        if button.styleSheet() == "yellow":
            button.setStyleSheet("background-color : red")
        else:
            button.setStyleSheet("background-color : yellow")
        pass

    def create_label(self):
        label = QtWidgets.QLabel(self)
        label.setObjectName("Update Label")
        label.setMinimumWidth(500)
        label.setMaximumHeight(100)
        label.setFrameStyle(Sunken)
        return label