# main routine goes here

# set max num of tickets below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter your name or 'XXX' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} tickets/s.  There are {} remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))