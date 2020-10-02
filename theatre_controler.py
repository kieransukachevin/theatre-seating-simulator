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
                self.connect_row_buttons()
                self.connect_column_buttons()
            else:
                view.popup_msg("The max number of rows is " + str(MAX_ROWS) + " and columns is " + str(MAX_COLUMNS))
        except ValueError:
            view.popup_msg("Enter numbers for rows and columns")
    
    def connect_seat_buttons(self):
        for key in self.window.seat_buttons:
            new_seat = Seat(False, self.model.price)
            self.model.seats[self.window.seat_buttons[key].text()] = new_seat
            self.window.seat_buttons[key].pressed.connect(
                lambda key=self.window.seat_buttons[key].text(): self.check_state(key)
            )

    def connect_row_buttons(self):
        for key in self.window.row_buttons:
            new_row = Seat(False, self.model.price * self.model.num_cols)
            self.model.rows[self.window.row_buttons[key].text()] = new_row
            self.window.row_buttons[key].pressed.connect(
                lambda key=self.window.row_buttons[key].text(): self.sell_row(key)
            )

    def connect_column_buttons(self):
        for key in self.window.col_buttons:
            new_col = Seat(False, self.model.price * self.model.num_rows)
            self.model.cols[self.window.col_buttons[key].text()] = new_col
            self.window.col_buttons[key].pressed.connect(
                lambda key=self.window.col_buttons[key].text(): self.sell_column(key)
            )

    def check_state(self, key):
        if self.model.seats[key].state == False:
            self.sell_seat(key)
            self.window.update_display_box("Seat " + key + " sold for $" + str(self.model.price), self.model.total_revenue)
        else:
            self.refund_seat(key)
            self.window.update_display_box("Seat " + key + " refunded", self.model.total_revenue)

    def sell_seat(self, key):
        if self.model.seats[key].state == False:
            self.model.total_revenue += self.model.seats[key].price
            self.model.seats[key].state = True
            self.window.display_box.repaint()
            self.window.button_pressed_style(self.window.seat_buttons[key])

    def refund_seat(self, key):
        if self.model.seats[key].state == True:
            self.model.total_revenue -= self.model.price
            self.model.seats[key].state = False
            self.window.display_box.repaint()
            self.window.button_default_style(self.window.seat_buttons[key])

    def sell_row(self, key):
        if self.model.rows[key].state == False:
            for i in range(self.model.num_cols):
                seat_name = key + str(i + 1)
                self.sell_seat(seat_name)
            self.model.rows[key].state = True
            self.window.update_display_box("Row " + key + " sold.", self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_pressed_style(self.window.row_buttons[key])
        else:
            for i in range(self.model.num_cols):
                seat_name = key + str(i + 1)
                self.refund_seat(seat_name)
            self.model.rows[key].state = False
            self.window.update_display_box("Row " + key + " refunded.", self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_default_style(self.window.row_buttons[key])

    def sell_column(self, key):
        seat_letter = 'A'
        if self.model.cols[key].state == False:
            for i in range(self.model.num_rows):
                self.sell_seat(seat_letter + str(key))
                seat_letter = chr(ord(seat_letter) + 1)
            self.model.cols[key].state = True
            self.window.update_display_box("Column " + key + " sold.", self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_pressed_style(self.window.col_buttons[key])
        else:
            for i in range(self.model.num_rows):
                self.refund_seat(seat_letter + str(key))
                seat_letter = chr(ord(seat_letter) + 1)
            self.model.cols[key].state = False
            self.window.update_display_box("Column " + key + " refunded.", self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_default_style(self.window.col_buttons[key])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    controller = TheatreController(view)
    sys.exit(app.exec_())