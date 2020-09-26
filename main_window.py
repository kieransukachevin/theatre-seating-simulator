from theatre_view import MainView, SeatsView
from PyQt5.QtWidgets import QApplication
import sys

MAX_ROWS = 25
MAX_COLUMNS = 30

class TheatreModel:
    def __init__(self):
        self.numSeats = 0
        self.windows = []
        self.topButtons = []
        self.sideButtons = []
        self.seats = []

class Seat:
    def __init__(self, button, state, row_price):
        self.is_taken = state
        self.price = row_price
        self.button = button

    def get_push_button(self):
        return self.button

class TheatreController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.init_controller()

    def init_controller(self):
        view.generateButton.clicked.connect(self.generate_button_clicked)

    def generate_button_clicked(self):
        try:
            rows = view.lineRow.text()
            cols = view.lineCol.text()
            rows = int(rows)
            cols = int(cols)
            if (rows > MAX_ROWS) or (cols > MAX_COLUMNS):
                view.popup_msg("The max number of rows is " + str(MAX_ROWS) + " and columns is " + str(MAX_COLUMNS))
            else:
                newWindow = SeatsView()                
                newModel = TheatreModel()
                self.generate_top_buttons(newWindow, newModel, cols)
                self.generate_side_buttons(newWindow, newModel, rows)
                self.generate_seats(newWindow, newModel, rows, cols)
        except ValueError:
            view.popup_msg("Enter numbers for rows and columns")

    def generate_top_buttons(self, newWindow, newModel, cols):
        for i in range(cols):
            button = newWindow.create_seat_button(str(i + 1), "red")
            newWindow.gridLayout.addWidget(button, 1, i + 2)
            newModel.topButtons.append(button)

    def generate_side_buttons(self, newWindow, newModel, rows):
        row_name = 'A'
        for i in range(rows):
            button = newWindow.create_seat_button(row_name, "red")
            newWindow.gridLayout.addWidget(button, i + 2, 0)
            newModel.sideButtons.append(button)
            row_name = chr(ord(row_name) + 1)

    def generate_seats(self, newWindow, newModel, rows, cols):
        row_name = 'A'
        newWindow.gridLayout.addWidget(newWindow.create_label(), 0, 0)
        newWindow.gridLayout.setRowStretch(0, 1)
        newWindow.gridLayout.setColumnStretch(0, 1)
        for i in range(rows):
            row = []
            for j in range(cols):
                button = Seat(newWindow.create_seat_button(row_name + str(j + 1), "yellow"), False, 0)
                row.append(button)
                newWindow.gridLayout.addWidget(button.get_push_button(), i + 2, j + 1)
            newModel.seats.append(row)
            row_name = chr(ord(row_name) + 1)
        model.windows.append(newWindow)
        newWindow.centralWidget().setLayout(newWindow.gridLayout)
        newWindow.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = TheatreModel()
    view = MainView()
    controller = TheatreController(model, view)
    sys.exit(app.exec_())