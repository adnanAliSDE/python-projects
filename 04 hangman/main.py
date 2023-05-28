import getpass
hangman = ["______", "|    |", "|    |",
           "|    O", "|   \|/", "|    |", "|   / \\", " "]


word = getpass.getpass("Enter the word: ")
wordList = list(word.lower())

matched = 0
life = 0


def takeGuess():
    global life
    global matched
    if matched == len(word):
        print("You won")
        return
    guess = input("Enter the guessed word: ").lower()

    if guess in wordList:
        wordList.remove(guess)
        print(" ")
        print("Enter the next letter")
        matched += 1
        print("Progress {}/{}".format(matched, len(word)))
        takeGuess()

    else:
        life += 1
        for i in range(life):
            if life == 7:
                [print(x) for x in hangman]
                print("")
                print("You Lost")
                return
                break
            else:
                print(hangman[i])
        print("")
        print("")
        print("Wrong guess! \n {} attempts left \n".format(7-life))
        takeGuess()


takeGuess()

print(" ")
print("The word is: ", word)
print(" ")
print(" Game Ended")
