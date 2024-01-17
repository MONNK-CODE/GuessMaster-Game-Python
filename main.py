#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

secret_number = random.randint(1, 100)
guess = None
count = 0

while guess != secret_number:
    user_input = input("Guess the secret number between 1 and 100: ")

    # Check if the input is a valid number
    if user_input.isdigit():
        guess = int(user_input)
        count += 1

        if guess < secret_number:
            print("Too low!! Try Again")
        elif guess > secret_number:
            print("Too high! Try again.")
    else:
        print("Please enter a valid number.")

print(f"Congratulations! You guessed the secret number {secret_number} in {count} tries.")

