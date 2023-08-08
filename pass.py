import re

def weak_password(password):
    common_patterns = ["123456", "abc", "india", "abc123"]
    for pattern in common_patterns:
        if pattern in password:
            return True
    return False

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char.isalnum() == False for char in password)
    
    strength = 0
    feedback = []

    if length >= 6:
        strength += 1
    else:
        feedback.append("Password should be at least 6 characters.")

    if has_uppercase:
        strength += 1
    else:
        feedback.append("Include at least one uppercase.")

    if has_lowercase:
        strength += 1
    else:
        feedback.append("Include at least one lowercase.")

    if has_digit:
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    if has_special:
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    if weak_password(password):
        strength = 0
        feedback.append("Avoid using common patterns.")

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)

    if strength >= 3:
        print("Password is strong!")
    else:
        print("Password is weak. Please consider the following:")
        for item in feedback:
            print("- " + item)

if __name__ == "__main__":
    main()
