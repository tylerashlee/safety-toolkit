import re

def evaluate_password(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$ etc).")

    if password.lower() in ['password', '123456', 'qwerty']:
        feedback.append("Avoid common passwords.")

    if score >= 4:
        return 'Strong', feedback
    elif score >= 2:
        return 'Moderate', feedback
    else:
        return 'Weak', feedback
