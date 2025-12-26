def validate(value, rules): # rules is a list of functions
    for rule in rules:
        if not rule(value): # rule is callable
            return False # if just one rule fails, then the value is not valid 
    return True

def has_symbol(value):
    return '@' in value

def has_username(value):
    return len(value.split('@')[0]) > 0

def has_valid_domain(value):
    return '.' in value.split('@')[1] if '@' in value else False

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def in_grade_range(value):
    try:
        grade = float(value)
        return 0 <= grade <= 20
    except ValueError:
        return False

def has_capital_letters(value):
    return any(char.isupper() for char in value)

def has_lowercase_letters(value):
    return any(char.islower() for char in value)

def has_symbols(value):
    return any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?' for char in value)

def has_digits(value):
    return any(char.isdigit() for char in value)


# Examples of use:

email = input()
print(validate(email, [has_symbol, has_username, has_valid_domain]))

grade = input()
print(validate(grade, [is_number, in_grade_range]))

strong_password = input()
print(validate(strong_password, [has_capital_letters, has_lowercase_letters, has_symbols, has_digits]))


