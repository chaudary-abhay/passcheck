"""
Project: Password Strength Checker
Description: A beginner-friendly cybersecurity tool that evaluates password
strength and gives practical improvement suggestions.

Run:
    python Abhay_PasswordStrengthChecker.py
"""

import re
import secrets
import string
import getpass


def evaluate_password(password):
    """Return a score, strength label, and improvement suggestions."""
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters (12 or more is better).")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character, such as !, @, or #.")

    common_passwords = {
        "password", "password123", "12345678", "qwerty123",
        "admin123", "welcome123", "letmein"
    }
    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords because attackers try them first.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if not suggestions:
        suggestions.append("Good work. Keep this password unique to one account.")

    return score, strength, suggestions


def generate_password(length=16):
    """Generate a random password using cryptographically secure randomness."""
    if length < 12:
        raise ValueError("For better security, choose a length of at least 12.")

    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        # Ensure the generated password includes all major character classes.
        if (re.search(r"[a-z]", password) and
                re.search(r"[A-Z]", password) and
                re.search(r"\d", password) and
                re.search(r"[^A-Za-z0-9]", password)):
            return password


def main():
    print("=" * 48)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 48)
    print("1. Check a password")
    print("2. Generate a secure password")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        password = getpass.getpass("Enter password (input is hidden): ")
        score, strength, suggestions = evaluate_password(password)
        print(f"\nStrength: {strength} ({score}/6)")
        print("Suggestions:")
        for item in suggestions:
            print(f"- {item}")
        print("\nNote: This program checks locally and does not store your password.")
    elif choice == "2":
        try:
            length_text = input("Password length (default 16): ").strip()
            length = int(length_text) if length_text else 16
            print("\nGenerated password:", generate_password(length))
            print("Store it in a trusted password manager.")
        except ValueError as error:
            print("Error:", error)
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()
