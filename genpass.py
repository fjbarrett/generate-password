import random
import string

# Function to generate a secure password with validation and full randomness
def generate_password(length=32, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Define character sets
    upper_chars = string.ascii_uppercase if include_upper else ''
    lower_chars = string.ascii_lowercase if include_lower else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = '~!@#%&*()_+-=,.<>/?[]{};:' if include_special else ''
    
    all_chars = upper_chars + lower_chars + digit_chars + special_chars
    if not all_chars:
        raise ValueError("At least one character type must be included.")

    while True:
        # Generate a random password
        password = ''.join(random.choices(all_chars, k=length))

        # Validate the password
        if (not include_upper or any(c in upper_chars for c in password)) and \
           (not include_lower or any(c in lower_chars for c in password)) and \
           (not include_digits or any(c in digit_chars for c in password)) and \
           (not include_special or any(c in special_chars for c in password)):
            return password

# Generate and display a password
try:
    password = generate_password(length=16, include_upper=True, include_lower=True, include_digits=True, include_special=True)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
