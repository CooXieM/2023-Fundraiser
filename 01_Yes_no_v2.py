# Function goes here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes / No")

# Main Routine Goes Here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ").lower()

    if want_instructions == "yes":
        print("Instructions")

    print("Program Continues...")
    print()