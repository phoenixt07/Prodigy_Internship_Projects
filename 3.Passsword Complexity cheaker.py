#code by @rushiaj_thorat
import re
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))
    common_patterns = ["password", "123456", "qwerty", "letmein", "admin", "welcome"]

   
    common_patterns_criteria = not any(pattern in password.lower() for pattern in common_patterns)

    # Calculate score
    score = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria, common_patterns_criteria])


    if score == 6:
        strength = "Very Strong"
    elif score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback message
    feedback = {
        "Very Strong": "Your password is very strong.",
        "Strong": "Your password is strong, but it could be improved.",
        "Moderate": "Your password is moderate. Consider adding more diverse characters.",
        "Weak": "Your password is weak. Try to make it longer and add more diverse characters.",
        "Very Weak": "Your password is very weak. Avoid common patterns and use a mix of characters."
    }

    return {
        "Password": password,
        "Score": score,
        "Strength": strength,
        "Feedback": feedback[strength]
    }

# Example usage
password = input("Enter a password to assess its strength: ")
assessment = assess_password_strength(password)
print(f"Password: {assessment['Password']}")
print(f"Score: {assessment['Score']}/6")
print(f"Strength: {assessment['Strength']}")
print(f"Feedback: {assessment['Feedback']}")
print("   ^    ")
print("   !    ")
print("   !    ")
print("***THIS TOOL MADE BY @rushiraj_thorat***")
