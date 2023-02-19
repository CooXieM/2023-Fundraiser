# Function goes here


# Main Routine Goes Here
while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("instructions goes here")
    elif want_instructions == "no" or want_instructions == "n":
        pass
    else:
        print("Please answer Yes / No")
print("We're Done")