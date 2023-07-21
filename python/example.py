import random
import os


class number_guessing:
    def __init__(self, starting, ending):
        self.start = starting
        self.end = ending
        self.chances = 0

    def mode(self):
        # increment = 0
        number = random.randint(self.start, self.end)
        select_mode = int(
            input("Select your mode :\n1.Easy.\n2.Intermediate.\n3.Hard.\n")
        )
        os.system("clear")

        if select_mode == 1:
            self.chances = 10
            print(f"you have {self.chances} chances to guess the number! ")
        elif select_mode == 2:
            self.chances = 7
            print(f"you have {self.chances} changes to guess the number! ")
        elif select_mode == 3:
            self.chances = 5
            print(f"you have {self.chances} changes to guess the number! ")
        else:
            print("select valid mode : ")
        while self.chances > 0:
            user_number = int(input("Enter guess number: "))
            if number > user_number:
                print("Your number is too Small.")
            elif number < user_number:
                print("Your number is too high.")
            elif number == user_number:
                print(f"Congratulation you did it {self.chances} try.")
            self.chances -= 1
