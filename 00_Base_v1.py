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


# Main Routine Goes Here

# set max num of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# ask users if they want to see instructions

want_instructions = yes_no("Do you want to see the instructions")

if want_instructions == "yes":
    print("Enter your name and then your age, thank you:")

print("\n program continues")
print()
# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    # Checks and ask the user how old they are

    age = num_check("How old are you?: \n")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("are you a ghost? please try again")
        continue

# calculate the price of the tickets using the users age:
age = int(input("How old are you?"))
if age < 12:
    price = 7.50
elif age > 16:
    price = 10.50
else:
    price = 6.50
print("The price of your ticket is: " + str(price))

tickets_sold += 1
# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} tickets/s.  There are {} remaining.".format(tickets_sold, MAX_TICKETS - tickets_sold))
