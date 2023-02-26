# function goes here


# check user enters an integer


def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")

# main routine goes here


tickets_sold = 0
while True:

    name = input("enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young for this movie")
        continue
    else:
        print("are you a ghost? please try again")
        continue

    tickets_sold += 1