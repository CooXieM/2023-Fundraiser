# checks that user enters a valid response (yes / no)
# cash credit based on a list of options
def string_checker(question, num_letters, valid_response):
    error = f"Please check {valid_response[0]} or {valid_response[1]}"

    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine goes here
yes_no_list = ["yes", "no"]
cash_credit = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("do you want to read the instructions", 1, yes_no_list)

    print("You chose", want_instructions)

for case in range(0, 5):
    payment_type = string_checker("Choose what payment type (Cash / Credit", 2, cash_credit)

    print("You chose", payment_type)
