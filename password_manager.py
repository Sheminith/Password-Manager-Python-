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
            f.write(f'{account} | {username} | {password}\n')
        print('Succesfully Added!')

# View item function
def view_item():
    found = False

    item_name = input('Enter Application/Website name to filter: ').lower()
    with open('password_list.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #remove any white space
            account, username, password = [x.strip().lower() for x in data.split('|')]

            if item_name == account:
                print(f'Website/application : {account}\n Username : {username}\n Password : {password}')
                found = True
    if not found:
        print('No results found!')

# Introducing the user to the application
print('Welcome to your password manager!')
user_inp = input('New / View / Delete / All / Quite(q) : ').lower()

while True:
    if user_inp == 'new':
        new_item()
    elif user_inp == 'view':
        view_item()
    elif user_inp == 'q' or user_inp == 'quit':
        break
