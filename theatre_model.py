class TheatreModel:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.top_buttons = []
        self.side_buttons = []
        self.seats = []

class Seat:
    def __init__(self, state, price):
        self.state = state
        self.price = price