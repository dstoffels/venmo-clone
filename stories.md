<!-- (5 points): As a data analyst, I want to create two Python Dictionaries called user_one and user_two that will represent the two users making and receiving payments from each other. Each dictionary will have the following identical keys (with the data type of the corresponding value in parenthesis):
- full_name (string)
- username (string)
- password (string)
- account_balance (integer)
- connected_banks: List of Tuples 
Each Tuple will have two elements:
- Name of the bank (string)
- Available balance (integer)
- EXAMPLE: (“Bank of America”,  200) -->

<!-- (5 points): As user_one, I want to be prompted to enter my username and password as input. If the username or password are not entered correctly, I want to be re-prompted until I enter them correctly. -->

<!-- (2.5 points): As user_one, I want to see my current account_balance printed to the console. -->

<!-- (10 points): As user_one, I want to see all of my connected_banks and their available funds in the following format: 
“Name of Bank: $XX” (where $XX represents the available balance of that account) -->

<!-- (5 points): As user_one, I want to be prompted to confirm that I would like to proceed with a transfer to user_two.If I choose not to proceed, the program ends. -->

<!-- (5 points): As user_one, I want to be prompted for how much money I want to transfer to user_two. If I don’t have enough money in my account_balance, re-prompt until I enter a value that I have sufficient funds to cover. -->

<!-- (5 points): As user_one, I want to subtract the transferred funds from my account balance and add them to user_two’s account_balance. -->

<!-- (5 points): As user_one, I want to be prompted to see if I want to make another transfer to user_two. If I do not make another transfer to user_two, I want to print my final account balance, then exit the application. -->

# Bonus Stories
(5 points): As a data analyst, I want to choose at the start of the program which user will make the transfer, and which user will receive the transfer.

(7.5 points): As a data analyst, I want to prompt the user to transfer money from a connected_bank to the account_balance if they don’t have sufficient funds to cover a transfer.

(7.5 points): As a data analyst, I want to prompt the user to transfer money from their account_balance to a connected_bank of their choosing at the end of a transaction.

(10 points): As a data analyst, I want to convert all of my code so that everything is written in functions.
Dictionaries can be outside of functions.
Try to split up your code into multiple functions that have a single responsibility (do one thing and do it well).
