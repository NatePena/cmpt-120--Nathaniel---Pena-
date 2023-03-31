def is_equilateral(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
    return x == y == z


def get_vowels(text):
    vowels = [char for char in text.lower() if char in 'aeiou']
    return vowels


def validate_list(grades):
    if type(grades) != list:
        raise TypeError("Grades must be a list")
    if not grades:
        raise ValueError("Grades list cannot be empty")
    for grade in grades:
        if type(grade) != int:
            raise TypeError("Grades must be integers")
        if grade < 0 or grade > 100:
            raise ValueError("Grades must be between 0 and 100")
    return grades


def is_palindrome(text):
    if type(text) != str:
        raise TypeError("Input must be a string")
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum())
    return text == text[::-1]


def calculate_letter_grade(grades):
    validate_list(grades)
    average = sum(grades) / len(grades)
    if average >= 93:
        return "A"
    elif average >= 90:
        return "A-"
    elif average >= 87:
        return "B+"
    elif average >= 83:
        return "B"
    elif average >= 80:
        return "B-"
    elif average >= 77:
        return "C+"
    elif average >= 73:
        return "C"
    elif average >= 70:
        return "C-"
    elif average >= 67:
        return "D+"
    elif average >= 63:
        return "D"
    elif average >= 60:
        return "D-"
    else:
        return "F"
