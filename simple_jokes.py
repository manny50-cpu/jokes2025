#!/usr/bin/env python3
"""Simple supplement: a minimal interactive knock-knock jokes script.

Demonstrates:
- List usage (JOKES dictionary of lists)
- Functions with parameters and return values
- Iteration (for loops)
- Selection (if/else)
- Input / output

Run: python3 simple_jokes.py
"""

JOKES = {
    "robbers": [("Calder", "Calder police - I've been robbed!")],
    "tanks": [("Tank", "You're welcome!")],
    "pencils": [("Broken pencil", "Nevermind, it's pointless!")],
}


def list_categories():
    """Return available categories (uses a list)."""
    return list(JOKES.keys())


def tell_category_jokes(category: str) -> None:
    """Tell every joke in the given category (demonstrates iteration)."""
    jokes = JOKES.get(category, [])
    if not jokes:
        print("Sorry, no jokes for that category.")
        return
    for setup, punch in jokes:
        input("Knock Knock ")
        input(setup + " ")
        print(punch)


def ask_rating() -> None:
    """Ask for a 1-10 rating and show percent (demonstrates selection & validation)."""
    while True:
        try:
            r = int(input("Please rate the game 1-10: ").strip())
            if 1 <= r <= 10:
                print(f"{r * 10} percent satisfaction rate")
                break
        except ValueError:
            pass
        print("Enter a whole number between 1 and 10.")

    rec = input("Would you recommend this game to a friend? (yes/maybe/no) ").strip().lower()
    if rec in ("yes", "maybe"):
        print("Thanks, we appreciate it.")
    else:
        print("Sorry you did not enjoy it.")


def main() -> None:
    """Minimal interactive loop using the helper functions."""
    print("Simple Knock-Knock Game!")
    while True:
        want = input("Do you want to hear a joke? (yes/no) ").strip().lower()
        if want != "yes":
            print("Okay, bye!")
            return

        print("Categories:", ", ".join(list_categories()))
        cat = input("Which category? ").strip().lower()
        tell_category_jokes(cat)

        again = input("Another? (yes/no) ").strip().lower()
        if again != "yes":
            ask_rating()
            return


if __name__ == "__main__":
    main()
