


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

jokes = [
    ["Knock Knock, Calder, Calder police - I've been robbed!"],
         ["Knock Knock, Tank, You're welcome!"],
         ["Knock Knock, Broken pencil, Nevermind it's pointless!"]]
def joke(lol):
    if lol == "robbers":
        input("Knock Knock")
        input("Calder")
        print("Calder police - I've been robbed!")
    elif lol == "tanks":
        input("Knock Knock")
        input("Tank")
        print("You are welcome!")
    elif lol == "pencils":
        input("Knock Knock")
        input("Broken pencil")
        print("Nevermind, it's pointless!")
    else:
        print("Sorry, I'm not funny enough for that.")

def finished(lol2):
    while lol2 == "yes":
        question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
        joke(question)
        lol2 = input("Do you want to hear another joke or are you finished? ")
    if lol2 == "no":            rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")

print("Thank you for playing the Knock Knock Joke Game!")



question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
joke(question)
question2 = input("Do you want to hear another joke or are you finished? ")
finished(question2)
