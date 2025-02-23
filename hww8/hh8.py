# Быки и коровы
import random

numbers = list(range(10))
random.shuffle(numbers)

comp_number = ""
for i in set(numbers[:4]):
    comp_number += str(i)

print("Computer made the 4 digit number, try to guess it!")

bulls = 0
while bulls != 4:
    guess_number = input("Enter 4 digit number with different digits: ")
    if (len(guess_number) != 4 or not guess_number.isdigit() or
            len(set(guess_number)) != 4):
        print("Enter valid 4 digit number")
        continue

    bulls = 0
    cows = 0
    index = 0

    for x in range(len(guess_number)):
        if guess_number[x] == comp_number[x]:
            bulls += 1
        elif guess_number[x] in comp_number:
            cows += 1
    print(f"{bulls} bull(s), {cows} cow(s). Try again!")

    if bulls == 4:
        print(f"You win, made up number: {comp_number}")
        break

# Пирамида
n = 10

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Статуи
statues = [6, 2, 3, 8]
min_statue = min(statues)
max_statue = max(statues)
amount_of_needed_statues = 0

for i in range(min_statue, max_statue):
    if i not in statues:
        amount_of_needed_statues += 1

print(amount_of_needed_statues)
