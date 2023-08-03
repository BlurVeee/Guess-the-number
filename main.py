import random
Correct_Number = (random.randint(1, 1000000))

print("Welcome to my Guess The Number Game")
print()
print("In this game, the goal is to guess the number with the less attemps as possible")
print("Quick reminder that the number IS NOT in the negative")
print()
print("Good luck :)")
print()
print()

attempts =+ 1
while True:
  number = int(input("Try guessing the number: "))
  if number == Correct_Number:
    print()
    print("CORERECT,", Correct_Number, "was indeed the random Number")
    if attempts == 1:
      print(("GOOD JOB. You did it in", attempts, "attemps"))
    elif attempts <= 20:
      print("that very good you did it in only", attempts, "attemps")
    else:
      print("You, could have been better, you did it in", attempts, "attemps")
    break
    exit()

  elif number > Correct_Number:
    print()
    print("Too high, Try again")
    print()
    attempts += 1

  elif number < Correct_Number:
    print()
    print("IT too low, try again")
    print()
    attempts += 1

