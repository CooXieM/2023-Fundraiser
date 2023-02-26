# Function goes here
def cash_card(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            cash_card("Choose a payment method (Cash / Card): ")
            return "cash"
        elif response == "card" or response == "cr":
            return "card"
        else:
            print("Please enter Cash or Card")

    # Main routine goes here
    while True:
        pass









