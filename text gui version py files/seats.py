class Seat:
    def __init__(self, state, row_price):
        self.is_taken = state
        self.price = row_price

def display_seats(all_seats):
    # define variable for whitespace spacing
    print("\nSeats: ")
    x = ' '

    # print digits of ten
    size = len(all_seats[0]) + 1
    print("\t0", end='')
    indicator = 1
    for i in range(1, size):
        if i / 10 == 1:
            print("\t", indicator, end='')
            indicator = indicator + 1
        elif i % 10 == 0:
            print(x*8, indicator, end='')
            indicator = indicator + 1
    
    # print single digits
    print(" ")
    print("\t1", end='')
    for i in range(2, size):
        print(i % 10, end='')
    
    # print rows
    size = len(all_seats) + 1
    print(" ")
    for i in range(1, size):
        if i < 10:
            print("Row: ", x, i, x, end='', sep='')
        else:
            print("Row: ", i, x, end='', sep='')
        for j in all_seats[i-1]:
            if j.is_taken:
                print('*', end='')
            else:
                print('#', end='')
        print(' ')

def sell_individual_ticket(all_seats):
    # sell an individual seat. Display revenue
    while True:
        try:
            row = input("Which row?:")
            row = int(row)

            seat = input("Which column?:")
            seat = int(seat)

            if all_seats[row - 1][seat - 1].is_taken == False:
                all_seats[row - 1][seat - 1].is_taken = True
                print("Row ", row, " seat ", seat, " sold for $", all_seats[row - 1][seat - 1].price, sep='')
            else:
                print("\nSeat already sold")
            break
        except ValueError:
            print("\nError: Enter an integer")
        except IndexError:
            print("\nError: Enter a valid row and seat")

def sell_row(all_seats):
    # sell a row. Display revenue
    while True:
        try:
            row = input("Which row?:")
            row = int(row)
            total_price = 0
            for i in all_seats[row - 1]:
                if i.is_taken == False:
                    i.is_taken = True
                    total_price = total_price + i.price
            print("\nRow ", row, " sold for $", total_price, sep='')
            break
        except ValueError:
            print("\nError: Enter an integer")
        except IndexError:
            print("\nError: Enter a row that exists")

def sell_ticket(all_seats):
    # choose to sell seat or row
    while True:
        display_seats(all_seats)
        choice = input("Sell individual seat, a whole row, or stop selling?(s, r, or q):")        
        if (choice == 's' or choice == 'S') == True:
            sell_individual_ticket(all_seats)
        elif (choice == 'r' or 'R') == True:
            sell_row(all_seats)
        elif (choice == 'q' or 'Q') == True:
            break
        else:
            print("\nError: Enter s, r, or q")

def display_stats(all_seats):
    # Display statistics
    avail_seats = 0
    taken_seats = 0
    total_rev = 0
    for i in all_seats:
        for j in i:
            if j.is_taken == True:
                taken_seats += 1
                total_rev += j.price
            else:
                avail_seats += 1
    print("\nThere are ", taken_seats, " tickets sold, ", avail_seats, " seats still available, and the total revenue is $", total_rev, sep='')
