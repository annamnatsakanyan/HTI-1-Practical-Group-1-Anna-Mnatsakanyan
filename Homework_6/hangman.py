import random

fruits = ["apple", "apricot", "avocado", "banana", "blackberry", "blackcurrant", "blueberry", "boysenberry",
          "cherry", "coconut", "grape", "grapefruit", "kiwifruit", "lemon", "lime", "lychee", "mandarin",
          "mango", "melon", "nectarine", "orange", "papaya", "peach", "pear", "pineapple", "plum", "pomegranate",
          "quince", "raspberry", "strawberry", "watermelon"]

fruits_choice = random.choice(fruits)
failed = 0
guesses = " "
failed_step = 5
while failed_step > 0:
    for char in fruits_choice:
        if char in guesses:
            print(char, end="")
        else:
            print(" _ ", end="")
            failed += 1

    print()
    guess = input("enter the guess character: ")
    guesses += guess

    if guess not in fruits_choice:
        failed_step -= 1
        if failed_step == 0:
            print("You didn't guess! ")

