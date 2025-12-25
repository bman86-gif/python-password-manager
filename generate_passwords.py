"""
collect user preferences,
- length
- should it contain uppercase?
- should it contain special chars?
- should it contain digits?

get all available characters
randomly pick characters up to the length
ensure that we have at least one of each of whatever the user selects.
ensure length is valid

"""


import random
import string


def generate_password():
    while True:
        length = int(input("Enter the desired password length: ").strip())
        if length >= 4:
            break
        print("Password length must be at least 4 characters.")


    characters = string.ascii_lowercase
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()

    if include_uppercase == "yes":
        characters += string.ascii_uppercase
        # print(f"[DEBUG] The value of characters is {characters}")
    if include_special == "yes":
        characters += string.punctuation
        # print(f"[DEBUG] The value of characters is {characters}")
    if include_digits == "yes":
        characters += string.digits
        # print(f"[DEBUG] The value of characters is {characters}")

    password = ""

    for i in range(length):
        password += random.choice(characters)
    password_list = list(password)
    if include_uppercase == "yes" and not any(c.isupper() for c in password_list):

        position = random.randint(0, length - 1)
        password_list[position] = random.choice(string.ascii_uppercase)

    if include_digits == "yes" and not any(c.isdigit() for c in password_list):
        position = random.randint(0, length - 1)
        password_list[position] = random.choice(string.digits)

    if include_special == "yes" and not any(c in string.punctuation for c in password_list):
        position = random.randint(0, length - 1)
        password_list[position] = random.choice(string.punctuation)

    password = "".join(password_list)

    return password



