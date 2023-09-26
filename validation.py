import re
# for password validation
lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spe_char = ["&", "*", "{", "}", "[", "]", ",", "=", "-", "(", ")", ".", "+", ";", "'", "/"]
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# function to validate email
def emailcheck(id):
    email_pattern = "^[a-z0-9._]+@[a-z]+.+[a-z]$"
    # Checking the input with pattern
    result = re.fullmatch(email_pattern, id)
    if result:
        return "valid"
    else:
        return "invalid"


# function to validate bangladesh phone number
def bang_no_check(ph_num):
    phone_number_pattern = '^[0]{1}[0-9]{10}$'
    # Checking the input with pattern
    result = re.fullmatch(phone_number_pattern, ph_num)
    if result:
        return "valid"
    else:
        return "invalid"


# function to validate USA phone number
def usa_no_check(us_ph_num):
    phone_number_pattern = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
    # Checking the input with pattern
    result = re.fullmatch(phone_number_pattern, us_ph_num)
    if result:
        return "valid"
    else:
        return "invalid"


# Function to validate password
def password_check(pwd):
    pattern = "^[a-zA-Z0-9&*()+=-}{';/.,]{16}$"
    # Checking the input with pattern and
    # Condition like should have 16 character, atleast one special character,upper and lower cases, and nummeric in the password
    if re.search(pattern, pwd) and len(pwd) == 16:
        has_special = any(char in spe_char for char in pwd)
        has_uppercase = any(char in uc for char in pwd)
        has_lowercase = any(char in lc for char in pwd)
        has_numeric = any(char in n for char in pwd)
        # if above conditions pass it is valid else invalid
        if has_special and has_uppercase and has_lowercase and has_numeric:
            return "Valid"
        else:
            return "Invalid"
    else:
        return "Invalid"


# Call functions
password = input("Enter the Password: ")
print(password_check(password))

email = input("Enter the Email: ")
print(emailcheck(email))

bangladesh_ph_num = input("Enter the bangladesh phone number: ")
print(bang_no_check(bangladesh_ph_num))

USA_ph_num = input("Enter the USA phone number: ")
print(usa_no_check(USA_ph_num))
