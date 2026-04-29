def main():
    while True:
        try:
            user_status = input("Are you a new user (n) or a returning user (r)? ")
        except TypeError: print("Invalid input. Try again.")
        else:
            if user_status == 'n' or user_status == 'r':
                break
            else:
                print("Invalid input. Try again.")
    #login dictionaries
    #menu
    #score updates
if __name__ == "__main__":
    main()