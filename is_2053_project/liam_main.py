#python main.py
def main():
    import liam_class
    test_user = liam_class.liam()
    guess = test_user.guess()
    test_user.update_score(guess)
    print(f"score: {test_user.get_score()}")
if __name__ == "__main__":
    main()