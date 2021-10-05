from random import randrange
n = randrange(1000)
while True:
    a = int(input())
    if a == n:
      print("You win!")
    break
    print("Smaller" if (n < a) else "Bigger")

