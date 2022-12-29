user1 = {
    "full_name": "Doug Stoffels",
    "username": "drstoffels",
    "password": '12345',
    "account_balance": 200,
    "connected_banks": [
        ("UWCU", 500),
        ("Wells Fargo", 2100)
    ]
}

user2 = {
    "full_name": "Dan Stoffels",
    "username": "danimal",
    "password": '12345',
    "account_balance": 0,
    "connected_banks": [
        ("UWCU", 255),
        ("Wells Fargo", 1100)
    ]
}

password = ''
while password != user1["password"]:
    password = input(f'Please enter your password: ')

print(f'Welcome, {user1["full_name"]}.')
print(f'Balance: ${user1["account_balance"]}')

banks = ''
for bank in user1["connected_banks"]:
    banks += f'{bank[0]}: ${bank[1]}\n'

print(f'''Connected Banks:
{banks}''')

def bool_input(prompt):
    response = ''
    while response != "y" and response != "n":
        response = input(prompt + ' y/n\n')
    return response

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            prompt = 'Please enter a number'

confirmation_prompt = f'Would you like to send money to {user2["full_name"]}?'
response = bool_input(confirmation_prompt)

while response == 'y':
    prompt = 'How much money would you like to send? $'
    transfer_amount = 0
    while user1["account_balance"] < transfer_amount or transfer_amount == 0:
        transfer_amount = int_input(prompt)
        prompt = f'Insufficient funds. Please enter an amount ${user1["account_balance"]} or less: '

    user1["account_balance"] -= transfer_amount
    user2["account_balance"] += transfer_amount
    response = bool_input(f'Would you like to send more money to {user2["full_name"]}? ')

print(f'Have a good day, {user1["full_name"]}')
print(f'Account Balance: ${user1["account_balance"]}')