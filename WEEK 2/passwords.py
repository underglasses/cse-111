"""
MARCOS CHINGA | CSE 111 | WEEK 2 | PASSWORDS
"""

import os
import time

# Constants
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")

# Function to check if a word exists in a file
def word_in_file(word, filename, case_sensitive=False):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return False

# Function to check if word has any character from a given list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# Function to calculate complexity of password
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# Function to evaluate password strength
def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity. This is a good password.")
        return 5

    # Otherwise, compute strength based on complexity
    complexity_score = word_complexity(password)
    strength_score = 1 + complexity_score
    print(f"Password has a complexity score of {complexity_score}.")
    return strength_score

    # Function to simulate loading animation
def load_animation():
    print("\nAnalyzing password strength...\n")
    animation = ["■□□□□ 20%", "■■□□□ 40%", "■■■□□ 60%", "■■■■□ 80%", "■■■■■ 100%"]
    for i in range(len(animation)):
        time.sleep(0.5)
        print("\r" + animation[i % len(animation)], end="")
    print("\n")

# Main input loop
def main():
    print("\n===============================================")
    print("== Welcome to the Password Strength Checker! ==")
    time.sleep(1)
    print("You can enter passwords to check their strength.")   
    weak_password_count = 0

    while True:
        password = input("\n> Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            print(f"\n>     Session ended. You entered {weak_password_count} weak password(s). <")
            time.sleep(1)
            print("Thank you for using the Password Strength Checker!")
            time.sleep(1)
            print("===============================================\n")

            break
    
        load_animation()

        strength = password_strength(password)
        print(f"\n>Ⓜ️  Password Strength Score: {strength} (0 = worst, 5 = best)<\n")

        # Recommendations
        if strength <= 2:
            weak_password_count += 1
            print(">⚠️  Tip: Try using a longer password with a mix of UPPER, lower, digits, and special characters.\n")
        elif strength <= 4:
            print(">⚠️  Decent! Add more complexity or length to make it stronger.\n")
        else:
            print(">✅  Great job! Your password is strong.\n")

# Only run the main function if this file is the entry point
if __name__ == "__main__":
    main()