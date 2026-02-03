


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

joke_data = [
    ["robbers", "Calder", "Calder police - I've been robbed!"],
    ["tanks", "Tank", "You are welcome!"],
    ["pencils", "Broken pencil", "Nevermind, it's pointless!"]
]

# Function 1: Handles the logic of finding and telling the joke
# Uses Parameters and Selection (if/else)
def tell_joke(user_choice):
    found = False
    
    # Iteration: Loop through the list to find the matching joke
    for item in joke_data:
        if item[0] == user_choice:
            input("Knock Knock")      # Sequencing: Step 1
            input(item[1])            # Sequencing: Step 2
            print(item[2])            # Sequencing: Step 3
            found = True
    
    if not found:
        print("Sorry, I'm not funny enough for that.")

# Function 2: Handles the ending survey and score calculation
def run_survey():
    rate = int(input("Please rate our game 1-10! "))
    # Simple math for the satisfaction rate
    final_score = rate * 10
    print(str(final_score) + "% percent satisfaction rate")
    
    friend = input("Would you recommend this game to a friend? ")
    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it.")
    else:
        print("Sorry you did not enjoy it.")

# --- MAIN PROGRAM FLOW ---
print("Welcome to the Knock Knock Joke Game!")

playing = "yes"
# Iteration: The game continues as long as the user wants to hear jokes
while playing == "yes":
    choice = input("Do you want to hear a joke about robbers, tanks, or pencils? ").lower()
    tell_joke(choice)
    
    playing = input("Do you want to hear another joke? (yes/no) ").lower()

# Call the second function after the loop ends
run_survey()
print("Thank you for playing!")