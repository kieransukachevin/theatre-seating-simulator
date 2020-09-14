# Kieran Sukachevin
# CPTR 108
# Theatre Simulator
#
# run with "python3 main.py"
# **************************

# import seat class and set max theatre size
import seats
MAX_ROWS = 25       # must be 99 or less
MAX_COLUMNS = 30    # must be 99 or less

while True:
    # welcome message 
    print("\n****** Welcome to Theatre Simulator ******")

    # ask user for number of rows
    while True:    
        try:
            num_rows = input("\nHow many rows are in the theatre?\nRows:")
            num_rows = int(num_rows)
            if (num_rows <= MAX_ROWS) == True:
                break
            else :
                print("\nError: Max amount of rows is", MAX_ROWS)
        except ValueError:
            print("\nError: Enter an integer")

    # ask user for price of each row. Store each price
    prices = list()
    print("\nEnter the price for each row", end='')
    for i in range(0, num_rows):
        while True:
            try:
                print("\nRow ", i + 1, ":", end='', sep='')
                price_of_row = input()
                price_of_row = float(price_of_row)
                prices.append(price_of_row)
                break
            except ValueError:
                print("\nError: Enter a decimal number")

    # ask user for number of columns
    while True:
        try: 
            num_cols = input("\nHow many columns?\nColumns:")
            num_cols = int(num_cols)
            if (num_cols <= MAX_COLUMNS) == True:
                break
            else:
                print("\nError: Max amount of columns is", MAX_COLUMNS)
        except ValueError:
            print("\nEnter an integer")

    # create 2D list of seats
    all_seats = list()
    for i in range(0, num_rows):
        row = list()
        for j in range(0, num_cols):
            seat = seats.Seat(False, prices[i])
            row.append(seat)
        all_seats.append(row)

    # set flag for quitting program
    quit = False
    
    # get user input and do one of four processes
    while True: 
        print("\nWould you like to: \na) display a seating chart \nb) sell tickets \nc) display stats \nd) reset the seating and pricing (or end the simulator) \nEnter a, b, c, or d:", end='')
        choice = input()
        if (choice == 'a' or choice == 'A') == True:
            seats.display_seats(all_seats)
        elif (choice == 'b' or choice == 'B') == True:
            seats.sell_ticket(all_seats)
        elif (choice == 'c' or choice == 'C') == True:
            seats.display_stats(all_seats)
        elif (choice == 'd' or choice == 'D') == True:
            while True:
                print("\nWould you like to quit or restart the program? (q or r):")
                choice = input()
                if (choice == 'q' or choice == 'Q') == True:
                    quit = True
                    break
                elif (choice == 'r' or choice == 'r') == True:
                    break
                else:
                    print("\nError: Enter q or r")
            break
        else:
            print("\nError: Enter a, b, c, or d")

    # quit program
    if quit == True:
        break
