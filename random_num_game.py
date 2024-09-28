import random

print("str")
difficulty = input("What difficulty will you like? (E)ffortless, E(a)sy, (M)edium, (H)ard, (I)nsane, E(x)treme, (U)nreal, Im(p)ossible: ")
if difficulty.upper() == "E": # difficulties
    secret_num = random.randint(5, 25)
elif difficulty.upper() == "A":
    secret_num = random.randint(5, 49)
elif difficulty.upper() == "M":
    secret_num = random.randint(5, 69)
elif difficulty.upper() == "H":
    secret_num = random.randint(5, 140)
elif difficulty.upper() == "I":
    secret_num = random.randint(2, 300)
elif difficulty.upper() == "X":
    secret_num = random.randint(2, 1000)
elif difficulty.upper() == "U":
    secret_num = random.randint(2, 3965)
elif difficulty.upper() == "P":
    secret_num = random.randint(2, 8000)

secret_num_found = False
attempts = 0

while not secret_num_found: # check if you have the number
    guess = input("Guess a number: ")
    percentage_closeness = int((1 - (abs(secret_num - int(guess)) / abs(secret_num))) * 100)
    percentage_closeness = max(0, min(percentage_closeness, 100))
    if percentage_closeness == 100:
        print(f"The secret number was {secret_num}! congrats! You took {attempts} attempts to get the number.")
        secret_num_found = True
    else:
        print(f"You are {percentage_closeness}% close to the secret number!")
        attempts += 1
            