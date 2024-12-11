#    ADDITION GAME


from random import randint

print("Select your level")
a = input("Press H for HARD and E for EASY \n")

if a == "H":
    b = randint(1, 1000)
    c = randint(1, 1000)
    count = 0
    e = b + c
    
    while True:
        guess = int(input(f"Sum of {b} and {c}: \n"))
        if guess == e:
            count += 1
            print(f"Your answer is correct! Your score is {count}")
            b = e  # Keep b as the correct answer from previous guess
            c = randint(1, 1000)
            e = b + c
        else:
            print(f"Wrong answer. Your final score is {count}")
            break

if a == "E":
    b = randint(1, 100)
    c = randint(1, 100)
    count = 0
    e = b + c
    
    while True:
        guess = int(input(f"Sum of {b} and {c}: \n"))
        if guess == e:
            count += 1
            print(f"Your answer is correct! Your score is {count}")
            b = e  # Keep b as the correct answer from previous guess
            c = randint(1, 100)
            e = b + c
        else:
            print(f"Wrong answer. Your final score is {count}")
            break
