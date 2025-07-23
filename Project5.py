import random as rd

WORDS = ['kevin', 'estiven', 'yepes', 'villareal', 'developer']

# 🔧 FUNCTIONS
def choose_word(words):
    """🎯 Returns a random word from the list."""
    return rd.choice(words)

def create_blanks(word):
    """📝 Creates a list of underscores according to the length of the word."""
    return ["_"] * len(word)

def show_progress(blanks):
    """👀 Prints the current guessed word with spaces."""
    print("Word:", " ".join(blanks))

def update_blanks(word, blanks, letter):
    """
    ✏️ Replaces underscores with the letter when correct.
    Returns True if the letter was found in the word, False otherwise.
    """
    hit = False
    for i, c in enumerate(word):  # i = index (position), c = character
        if c == letter:
            blanks[i] = letter
            hit = True
    return hit

def is_word_complete(blanks):
    """✅ Returns True if there are no underscores left."""
    return "_" not in blanks
# 🎮 MAIN GAME LOGIC

def play_hangman(words=WORDS, lives=5):
    word = choose_word(words)
    blanks = create_blanks(word)

    print("🎉 Welcome to the Hangman Game!")
    show_progress(blanks)

    while lives > 0:
        letter = input("🔤 Type a letter to guess the word: ").lower().strip()
        if not letter:
            print("⚠️ You didn't type anything. Try again.")
            continue
        letter = letter[0]  # Only take the first character if user types more than one

        hit = update_blanks(word, blanks, letter)

        if hit:
            print(f"🎯 Great! The letter is in the word: {' '.join(blanks)}")
        else:
            lives -= 1
            print(f"❌ Not in the word: {' '.join(blanks)}. Lives left: {lives}.")

        if is_word_complete(blanks):
            print(f"🏆 Congratulations! You guessed the word: {word}")
            return True  # Win
    print(f"💀 Game over. The word was: {word}")
    return False  # Lose

# ▶️ RUN ONLY IF MAIN SCRIPT
if __name__ == "__main__":
    play_hangman()
