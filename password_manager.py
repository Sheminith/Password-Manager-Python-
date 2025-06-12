# Confirmation message function
def confirm():
    while True:
        user_inp = input('Confirm? (Yes/No) : ').lower()
        if user_inp == 'yes':
            return True
        elif user_inp == 'no':
            return False
        else:
            continue

# New item function
def new_item():
    account = input('Name of Website/Application: ')
    username = input('Email/Username: ')
    password = input('Password: ')

    user_confirmation = confirm()
    if user_confirmation == True:
        with open('password_list.txt', 'a') as f:
            f.write(f'{account} | {username} | {password} \n')
        print('Succesfully Added!')
    

# Introducing the user to the application
print('Welcome to your password manager!')
user_inp = input('New / View / Delete / All / Quite(q) : ').lower()

while True:
    if user_inp == 'new':
        new_item()
    elif user_inp == 'q' or user_inp == 'quit':
        break
