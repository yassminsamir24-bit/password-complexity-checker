password=input('enter your password:')
has_upper=False
has_lower=False
has_digit=False
has_special=False
special_char='!@#$%^&*'
for char in password:
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True
    if char.isdigit():
        has_digit=True
    if char in special_char:
        has_special=True
if len(password)>=10 and has_upper and has_lower and has_digit and has_special:
    print('password is valid')
else:
    print('password is not valid')
