# Password Strength Checker

## Project description
A beginner-friendly cybersecurity project that checks password strength and can
generate a random password using Python's cryptographically secure `secrets`
module. It gives feedback about length, uppercase/lowercase letters, numbers,
and special characters.

## Dataset
**No external dataset is required.** The project uses rule-based checks and a
small, clearly defined list of common-password examples inside the source code.
You can test it with passwords you create yourself. Do not use a real password
that protects an important account.

## Technologies used
- Python 3.9+
- Python standard library: `re`, `string`, `secrets`, `getpass`

## Setup
1. Install Python 3.9 or later.
2. Download `Abhay_PasswordStrengthChecker.py` and `requirements.txt`.
3. Open a terminal in the project folder.
4. (Optional) Create and activate a virtual environment.
5. Install listed dependencies (there are no third-party dependencies):
   ```bash
   pip install -r requirements.txt
   ```

## Run
```bash
python Abhay_PasswordStrengthChecker.py
```

Choose option `1` to check a password or option `2` to generate one.

## Key features
- Rates a password as Weak, Moderate, or Strong.
- Checks length and character variety.
- Warns about a few common example passwords.
- Generates passwords with Python's `secrets` module.
- Hides password input during checking.
- Does not save or transmit the entered password.

## Limitations and responsible use
This is an educational demonstration, not a complete enterprise password
auditor. It does not check breached-password databases, estimate cracking time,
or replace multi-factor authentication and a password manager. A strong
password should be unique for every account.
