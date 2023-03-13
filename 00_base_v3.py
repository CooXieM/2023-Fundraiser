import pandas
import random


# Checkers user has answered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes / No \n")


# checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again ")
            print()
        else:
            return response


# check user enters an integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# card / credit

def cash_card(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please pick Cash or Card")


# checks that user enters a valid response (yes / no)
# cash credit based on a list of options
def string_checker(question, num_letters, valid_response):
    error = f"Please check {valid_response[0]} or {valid_response[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main Routine Goes Here

# set max num of tickets below / tickets sold to 0
MAX_TICKETS = 30
tickets_sold = 0
# list yes/no list card/cash
yes_no_list = ["yes", "no"]
cash_credit = ["cash", "credit"]

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# set price and profit to 0
price = 0
profit = 0
# ask users if they want to see instructions
want_instructions = yes_no("Do you want to see the instructions")

if want_instructions == "yes":
    print("Enter your name and then your age, thank you:")

print("\n program continues")
print()
# ask users if they want to pay with cash or card

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nEnter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    # Checks and ask the user how old they are

    age = num_check(f"{name} How old are you?: \n")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print(f"sorry you are too young for this movie, come back in {12 - age} years ")
        continue
    else:
        print("are you a ghost? please try again")
        continue

    # state payment_type and ask user for card / cash

    payment_type = cash_card("\n please pick your payment type: Cash / Credit").lower()

    # calculate the price of the tickets using the users age:
    if 12 <= age <= 15:
        price = 7.50

    elif 16 <= age <= 64:
        price = 10.50

    elif age >= 65:
        price = 6.50

    if payment_type == "credit":
        surcharge = price * 0.05
    else:
        surcharge = 0

    profit += price
    # print("Your ticket price is: $" + str(price))
    print(f"Your ticket price is ${price:.2f}")

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(price)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting ( uses Currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose winner from list
winner_name = random.choice(all_names)

# get position of winner from our name list
win_index = all_names.index(winner_name)

# look up total amount won
total_won = mini_movie_frame.at[win_index, 'Total']

print("-----Ticket Data-----")
# output data table
print(mini_movie_frame)


# Print winner of the raffle and how much they won.
print('----- Raffle Winner -----')
print("Congratulations {}. you have won ${}..."
      "YOUR TICKET IS FREE".format(winner_name, total_won))
print()
# Decor
print()
print("----- Totals -----")
print()
# out put total sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total profit: ${:.2f}".format(profit))
print()

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print(f"Congratulations you have sold all the tickets. Your total profit is ${profit:.2f}")
else:
    print(f"You sold {tickets_sold} tickets, you have {MAX_TICKETS - tickets_sold} remaining.")
