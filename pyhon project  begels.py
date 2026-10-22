import random
print("welcome to Begels!")
player_name = "player"
print("Hello,",player_name)
secret = "".join(random.sample("0123456789", 3))
while secret[0] == "0":
   secret = "".join(random.sample("0123456789", 3))
won = False
for attempt in range(10):
    print(f"Attempt {attempt + 1}")
    guess = input("Guess a 3-digit number: ")
    while len(guess) != 3 or not guess.isdigit():
       print("please enter exactly 3 digits .")
       guess = input("Guess a 3 digit number: ")
    print("your guess is",guess)
    if guess[0] not in secret and guess[1] not in secret and guess[2] not in secret:
        print("Bagels")
    if guess[0] == secret[0]:
        print("Fermi!")
    if guess[1] == secret[1]:
        print("Fermi!")
    if guess[2] == secret[2]:
        print("Fermi!")
    if guess[0] in secret and guess[0] != secret[0]:
      print("Pico")
    if guess[1] in secret and guess[1] != secret[1]:
      print("Pico")
    if guess[2] in secret and guess[2] != secret[2]:
      print("Pico")
    if guess == secret:
       won = True
       print("you got it!")
       break
if not won:
   print("out of guesses! The secret was", secret)
