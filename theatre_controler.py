from theatre_view import MainView, SeatsView
from theatre_model import TheatreModel, Seat
from PyQt5.QtWidgets import QApplication
import sys

MAX_ROWS = 25
MAX_COLUMNS = 30

class TheatreController:
    def __init__(self, view):
        self.view = view
        self.init_controller()

    def init_controller(self):
        self.view.generate_button.clicked.connect(self.try_generate_button)

    def try_generate_button(self):
        try:
            num_rows = view.line_row.text()
            num_rows = int(num_rows)

            num_cols = view.line_col.text()
            num_cols = int(num_cols)

            price = view.seat_price.text()
            price = int(price)

            if (num_rows < MAX_ROWS) and (num_cols < MAX_COLUMNS):
                self.window = SeatsView(num_rows, num_cols)
                self.model = TheatreModel(num_rows, num_cols, price)
                self.connect_seat_buttons()
            else:
                view.popup_msg("The max number of rows is " + str(MAX_ROWS) + " and columns is " + str(MAX_COLUMNS))
        except ValueError:
            view.popup_msg("Enter numbers for rows and columns")
    
    def connect_seat_buttons(self):
        for i in range(self.model.num_rows):
            row = []
            for j in range(self.model.num_cols):
                self.window.seat_buttons[i][j].clicked.connect(self.sell_ticket)
                new_seat = Seat(False, self.model.price)
                row.append(new_seat)
            self.model.seats.append(row)

    def sell_ticket(self):
        button_name = 
        self.model.total_revenue += self.model.price
        self.window.update_label.setText("Total revenue is: " + str(self.model.total_revenue))
        self.window.update_label.repaint()
        print("ticket sold")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    controller = TheatreController(view)
    sys.exit(app.exec_())