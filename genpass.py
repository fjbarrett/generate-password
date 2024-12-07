import random

# Password Generation at length 32 with most special characters
def generate_password(length=32):
    hex_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_chars = '~!@#%&*()_+-=,.<>/?[]{};:'
    all_chars = hex_chars + special_chars
    password = random.choices(all_chars, k=length)
    return ''.join(password)

# Generate a 16-byte password and calculate its entropy
password = generate_password(16)

# Display entropy of the generated password
print(f"Generated Password: {password}")