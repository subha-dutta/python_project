

import random

random_number=random.randint(0,10)
attempt=3

print(random_number)

while attempt>0:
    user_input=int(input("Please enter any number from 0 to 10- "))
    attempt-=1
    print("your have left attempt",attempt)
    if user_input==random_number:
        print("you have guessed correct number!")
        break
    else:
        print("you have guessed worng number.")
print("correct anwer was",random_number)

