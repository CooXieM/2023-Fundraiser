# main routine goes here

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


# Check what payment they desire
def cash_card(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return response

        elif response == "card" or response == "cr":
            return response

        else:
            print("Please pick Cash or Card")


# Main Routine Goes Here

# set max num of tickets below / tickets sold to 0
MAX_TICKETS = 3
tickets_sold = 0
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
payment_type = cash_card("please pick your payment type: Cash / Card")

if payment_type == "cash" or payment_type == "ca":
    print("\n you chose cash")
elif payment_type == "card" or payment_type == "cr":
    print("\n you chose card")

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

    # calculate the price of the tickets using the users age:
    if 12 <= age <= 16:
        price = 7.50

    elif 16 <= age < 76:
        price = 10.50

    elif age >= 76:
        price = 6.50

    profit += price
    print("Your ticket price is: $" + str(price))

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print(f"Congratulations you have sold all the tickets. Your total profit is ${profit}")
else:
    print(f"You sold {tickets_sold} tickets, you have {MAX_TICKETS - tickets_sold} remaining.")
