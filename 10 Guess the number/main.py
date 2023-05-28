from random import randint
rng = input(
    "Please enter the range in which you want to guess the number or press d for default range(0-100): \n")

start = 0
stop = 100
if rng != 'd':
    start = int(rng.split("-")[0]) or 0
    stop = int(rng.split("-")[1]) or 100
    if (stop-start) < 9:
        raise ValueError("Please provide a valid range greater or equal to 10")
score = 0
while True:
    inp = input("Guess the number or press q to quit: ")
    if inp != 'q':
        inp = int(inp)
        num = randint(start, stop)
        if num == inp:
            print(f"Correct! You gained 1 point")
            score += 1
            print(f"Your score: {score}")
        else:
            score -= 1
            print("Wrong answer You lost 1 point")
    else:
        print("Game ended")
        print(f"Your score is {score}")
        break
