import random
import math

low = int(input("Enter Lower Number:-"))
high = int(input("enter Higher Number:-"))

x = random.randint(low, high)
print("\n \tYou've only ",
      round(math.log(high - low + 1, 2)),
    " chances to guess the integer! \n")

count = 0

while count < math.log(high - low + 1, 2):
    count+= 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congrats your the best in only ",
              count, " try")

        break
    elif x > guess:
        print("Your guess is Under!")
    elif x < guess:
        print("Your guess is Over!")

if count >= math.log(high - low +1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next Time!")