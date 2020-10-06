class TheatreModel:
    def __init__(self, num_rows, num_cols, price):
    	'''Initialize the model.'''

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.price = price
        self.total_revenue = 0
        self.seats = {}
        self.rows = {}
        self.cols = {}

class Seat:
    def __init__(self, state, price):
    	'''Initialize a seat in the model.'''

        self.state = state
        self.price = price