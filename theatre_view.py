from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QSettings
import sys

class MainView(QMainWindow):
    def __init__(self):
        # Initialize the window
        super(MainView, self).__init__()
        self.setWindowTitle("Theatre Generator")
        self.init_UI()
        self.init_menubar()
        self.show()

    def init_UI(self):
        # Do basic setups
        self.setGeometry(200, 200, 1000, 100)
        self.menu_layout = QtWidgets.QHBoxLayout()

        # Create line edit widget for parsing number of rows
        self.line_row = QtWidgets.QLineEdit(self)
        self.line_row.setObjectName("Rows")
        self.line_row.setPlaceholderText("Number of Rows")
        self.menu_layout.addWidget(self.line_row, 600)

        # Create line edit widget for parsing number of columns
        self.line_col = QtWidgets.QLineEdit(self)
        self.line_col.setObjectName("Columns")
        self.line_col.setPlaceholderText("Number of Columns")
        self.menu_layout.addWidget(self.line_col, 600)

        # Create line edit widget for parsing price of a seat
        self.seat_price = QtWidgets.QLineEdit(self)
        self.seat_price.setObjectName("Price")
        self.seat_price.setPlaceholderText("Price of a seat")
        self.menu_layout.addWidget(self.seat_price, 700)

        # Create push button for generating a new window
        self.generate_button = QtWidgets.QPushButton("generate", self)
        self.menu_layout.addWidget(self.generate_button, 300)

        # Set window layout to the horizontal layout with widgets added
        wid = QtWidgets.QWidget(self)
        self.setMenuWidget(wid)
        wid.setLayout(self.menu_layout)

    def init_menubar(self):
        # Initialize menubar of window
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
        x = msg.exec_()

class SeatsView(MainView):
    def __init__(self, num_rows, num_cols):
        super(MainView, self).__init__()
        self.setWindowTitle("Theatre Generator")
        self.setWindowIcon(QtGui.QIcon("kieran's logo.jpg"))
        self.seat_buttons = []
        self.row_buttons = []
        self.col_buttons = []
        self.init_UI(num_rows, num_cols)
        self.init_menubar()
        self.show()

    def init_UI(self, num_rows, num_cols):
        self.grid_layout = QtWidgets.QGridLayout()

        self.generate_update_box(num_rows)
        self.generate_top_buttons(num_cols)
        self.generate_side_buttons(num_rows)
        self.generate_seats(num_rows, num_cols)

        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)

    def create_seat_button(self, name, color):
        button = QtWidgets.QPushButton(self)
        button.setText(name)
        button.setMaximumSize(80, 40)
        button.setMinimumSize(30, 20)
        button.setStyleSheet("background-color : " + color)
        return button

    def create_label(self):
        label = QtWidgets.QLabel(self)
        label.setObjectName("Update Label")
        label.setMinimumWidth(500)
        label.setMaximumHeight(100)
        label.setFrameStyle(50)
        return label

    def generate_update_box(self, num_rows):
        self.grid_layout.addWidget(self.create_label(), 0, 0, num_rows, 0)
        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setColumnStretch(0, 1)
        print("update box created")

    def generate_top_buttons(self, num_cols):
        for i in range(num_cols):
            button = self.create_seat_button(str(i + 1), "red")
            self.grid_layout.addWidget(button, 2, i + 1)
            self.col_buttons.append(button)
        print("top buttons created")

    def generate_side_buttons(self, num_rows):
        row_letter = 'A'
        for i in range(num_rows):
            button = self.create_seat_button(row_letter, "red")
            self.grid_layout.addWidget(button, i + 3, 0)
            self.row_buttons.append(button)
            row_letter = chr(ord(row_letter) + 1)
        print("side buttons created")

    def generate_seats(self, num_rows, num_cols):
        # Create a grid of seat buttons num_cols tall and num_rows wide
        row_letter = 'A'
        for i in range(num_rows):
            new_row = []
            for j in range(num_cols):
                button = self.create_seat_button(row_letter + str(j + 1), "yellow")
                new_row.append(button)
                self.grid_layout.addWidget(new_row[j], i + 3, j + 1)
            self.seat_buttons.append(new_row)
            row_letter = chr(ord(row_letter) + 1)
        print("seates created")

    def seat_button_clicked(self, button):
        if button.styleSheet() == "yellow":
            button.setStyleSheet("background-color : red")
        else:
            button.setStyleSheet("background-color : yellow")
        pass