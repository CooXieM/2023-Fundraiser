# Function goes here

#check user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        #if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
            print()
        else:
            return response

# main routine goes here

# main routine
while True:
    name = not_blank("Enter your name or 'xxx' to quit")
    if name == "xxx":
        break

print("we are done")