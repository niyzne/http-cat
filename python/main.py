import script

while True:
    user_choice = input("Pick your choice:\n[1] print random status links\n[q] quit\nYour choice?: ")
    if user_choice == "1":
        script.random_links()
    elif user_choice == "q":
        break
    else:
        print("Invalid input, try again")
