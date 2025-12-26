def has_symbol(email: str):
    return email.count('@') == 1

def has_username(email: str):
    parts = email.split('@')
    username = parts[0] # before the @ symbol
    return len(username) > 0

def has_valid_domain(email: str):
    res = None
    parts = email.split('@')
    domain = parts[1]

    if domain.count('.') == 1: # considering only this type of emails
        domain_parts = domain.split('.')
        res = len(domain_parts[0]) > 0 and len(domain_parts[1]) > 0 

    else:
        res = False

    return res
    

def validate_email(email): # order is important (take advantage of short circuit evaluation)
    return has_symbol(email) and has_username(email) and has_valid_domain(email) 

def bad_validate_email(email):
    if email.count('@') != 1:
        return False
    
    parts = email.split('@')
    username = parts[0]

    if len(username) == 0:
        return False
    
    domain = parts[1]

    if domain.count('.') != 1: # considering only this type of emails
        return False
    
    domain_parts = domain.split('.')
    if len(domain_parts[0]) == 0 or len(domain_parts[1]) == 0:
        return False

    return True



