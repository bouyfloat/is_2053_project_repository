class liam:
    def __init__(self):
        self.score = 0
    def guess(self): #no return
        import random
        maximum_guess, score = 1, 0
        while True:
            while True:
                try:
                    user_guess = int(input(f"Enter your guess (0-{maximum_guess}): "))
                except ValueError:
                    print("Invalid guess. Try again.")
                else:
                    if user_guess >= 0 and user_guess <= maximum_guess: break
                    else: print("Invalid guess. Try again.")
            computer_guess = random.randint(0, maximum_guess)
            if computer_guess == user_guess:
                score += 1
                print(f"You guessed correctly. Your score is {score}")
                maximum_guess += 1
                continue
            else:
                print(f"You guessed incorrectly. Your score is {score}.")
                break
        return score
    def update_score(self, score): self.score += score
    def get_score(self): return self.score