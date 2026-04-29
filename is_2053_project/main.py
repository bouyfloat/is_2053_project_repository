def create_login():
    a=0
def get_score():
    a=0
def login():
    a=0
def update_score():
    a=0
def menu():
    print("Menu\n")
    print("0. End program")
    print("1. Log in")
    print("2. Create account")
    print("3. Play Kevin's game")
    print("4. Play Liam's game")
    while True: #user select menu item
        try:
            menu_item = int(input("Select a menu item: "))
        except TypeError: print("Invalid input. Try again.")
        else:
            if menu_item >= 0 and menu_item <= 4: break
            else: print("Invalid input. Try again.")
    #call menu item functions
def main():
    a=0
if __name__ == "__main__":
    main()