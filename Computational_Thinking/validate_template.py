def validate(value, rules): # rules is a list of functions
    for rule in rules:
        if not rule(value): # rule is callable
            return False # if just one rule fails, then the value is not valid 
    return True

# Examples of use (functions should be implemented for this to work)

email = input()
print(validate(email, [has_symbol, has_username, has_valid_domain]))

grade = input()
print(validate(grade, [is_number, in_grade_range]))

strong_password = input()
print(validate(strong_password, [has_capital_letters, has_lowercase_letters, has_symbols, has_digits]))