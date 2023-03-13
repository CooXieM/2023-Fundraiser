# Cash or credit function

def cash_credit(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'card' or response == 'ca':
            response = 'you chose card'
            return response
        elif response == 'cash' or response == "cash":
            response = 'no'
            return response
        else:
            print('Please choose Cash or Card')


print("You chose {} as your payment")
