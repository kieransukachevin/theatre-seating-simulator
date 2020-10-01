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
                # self.test_connect_seats()
            else:
                view.popup_msg("The max number of rows is " + str(MAX_ROWS) + " and columns is " + str(MAX_COLUMNS))
        except ValueError:
            view.popup_msg("Enter numbers for rows and columns")
    
    def connect_seat_buttons(self):
        for key in self.window.seat_buttons:
            new_seat = Seat(False, self.model.price)
            self.model.seats[self.window.seat_buttons[key].text()] = new_seat
            self.window.seat_buttons[key].pressed.connect(
                lambda key=self.window.seat_buttons[key].text(): self.sell_ticket(key)
            )

    def sell_ticket(self, key):
        if self.model.seats[key].state == False:
            self.model.total_revenue += self.model.price
            self.model.seats[key].state = True
            self.window.update_display_box("Seat " + key + " sold for $" + str(self.model.price), self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_pressed_style(self.window.seat_buttons[key])
        else:
            self.model.total_revenue -= self.model.price
            self.model.seats[key].state = False
            self.window.update_display_box("Seat " + key + " refunded", self.model.total_revenue)
            self.window.display_box.repaint()
            self.window.button_default_style(self.window.seat_buttons[key])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    controller = TheatreController(view)
    sys.exit(app.exec_())