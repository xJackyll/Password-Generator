# Author: Giacomo Caruso
# This is a Python script example
# It generates a random password of a specified length

import random
import string

def generate_password(length):
    """Generate a random password of a specified length"""
    # Define the character set to use for the password
    char_set = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by selecting characters randomly from the character set
    password = ''.join(random.choice(char_set) for i in range(length))
    
    return password

# Prompt the user to specify the length of the password they want to generate
length = int(input("Enter the length of the password you want to generate: "))

# Generate the password and display it to the user
password = generate_password(length)
print("Your randomly generated password is:", password)
