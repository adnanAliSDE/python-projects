from random import randint

# Game features to be added
# two modes - PvP, Computrerk


options = ["snake", "water", "gun"]
cases = {"draw": {["gun", "gun"], ["water", "water"], ["snake", "snake"]},
         "win": {["snake", "water"], ["water", "gun"], ["gun", "snake"]},
         "lose": {["snake", "gun"], ["water", "snake"], ["gun", "water"]}
         }

[print(i, "-", options[i]) for i in range(3)]

personChoice = int(
    input("Enter the index of your choice from above options: "))
if personChoice not in range(3):
    print("Please choose correct option")
computerChoice = randint(0, 2)
print(computerChoice)

choices = [options[personChoice], options[computerChoice]]

print(" ")
print("Your choice: ", choices[0])
print("Opponent choice: ", choices[1])
print(" ")
if choices in cases["win"]:
    print("You Won")
elif choices in cases["lose"]:
    print("You lost")
else:
    print("The game is draw")
