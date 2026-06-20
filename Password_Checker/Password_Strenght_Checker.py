# PASSWORD STRENGTH CHECKER


import re

# Requirments of a strong password:
# Min 8 Chars, digits, Uppercase, Lowercase, Spl. Chars.

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Pasword Must Contain 8 Chars."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password Must Contain a Digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: Password Must Contain a Uppercase"
    
    if not any(char.islower() for char in password):
        return "Weak: Password Must Contain a Lowercase"
    
    if not re.search(r'[!@#$%^&*().?]', password):
       return "Medium: Password Must Contain a Special Char."

    return "Congrats! Your Password Is Strong."

def password_chcker():
    print("Welcome To The Password Strenght Checker Tool.")

    while True:
        password = input("Enter Your Passwrod or (type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank You For Using This This Tool.")
            break
        result = check_password_strength(password)
        print(result)


# Run The Password Checking tool:

if __name__ == "__main__":
    password_chcker()        