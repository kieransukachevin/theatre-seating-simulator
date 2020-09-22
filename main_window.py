from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
MAX_ROWS = 25
MAX_COLUMNS = 30

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle("Theatre Generator")
        self.initUI()

    def initUI(self):
        self.gridLayout = QtWidgets.QGridLayout()   # create layout for central widget
        self.menuLayout = QtWidgets.QHBoxLayout()   # create layout for menubar

        self.lineRow = QtWidgets.QLineEdit(self)
        self.lineRow.setObjectName("Rows")
        self.lineRow.setPlaceholderText("Rows")
        self.menuLayout.addWidget(self.lineRow, 100)
        self.numRows = 5

        self.lineCol = QtWidgets.QLineEdit(self)
        self.lineCol.setObjectName("Columns")
        self.lineCol.setPlaceholderText("Columns")
        self.menuLayout.addWidget(self.lineCol, 200)
        self.numCols = 5

        self.generateButton = QtWidgets.QPushButton("generateButton", self)
        self.generateButton.clicked.connect(self.generate_button_clicked)
        self.menuLayout.addWidget(self.generateButton, 300)

        wid = QtWidgets.QWidget(self)
        self.setMenuWidget(wid)
        wid.setLayout(self.menuLayout)

    def generate_button_clicked(self):
        try:
            numRows = self.lineRow.text()
            numCols = self.lineCol.text()
            int(numRows)
            int(numCols)
            self.generate_seats(numRows, numCols)
        except ValueError:
            self.popup_msg("Enter numbers for rows and columns")

    def generate_seats(self, numRows, numCols):
        for i in range(int(numRows)):
            for j in range(int(numCols)):
                button = QtWidgets.QPushButton(self)
                button.setText("seat")
                button.setMaximumSize(80, 40)
                button.clicked.connect(self.seat_button_clicked)
                self.gridLayout.addWidget(button, i, j)
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(self.gridLayout)

    def update(self):
        self.label.adjustSize()

    def seat_button_clicked(self):
        pass

    def popup_msg(self, message):
        msg = QMessageBox()
        msg.setGeometry(500, 300, 500, 100)
        msg.setWindowTitle("Error")
        msg.setText("Error")
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(QMessageBox.Ignore)
        msg.setInformativeText(message)

        x = msg.exec_() # executes message box
    

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()