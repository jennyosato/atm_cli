import random

   
print('Welcome to FCMB ATM cli')
print('========================')
db = []
num = '0123456789'
length = 10
account = ''
 
while True:
 print('Create an Account')
 create = int(input('Enter 1 to Create Account:'))
 if create == 1:
    for acct in range(length):
     account += random.choice(num)
    bal = 1000
    user = {'account_number': account, 'balance': bal}
    db.append(user)
    print('\nAccount Created successfully')
    print('Your account number is:' + ' ' + user['account_number'])
    account = ''
    while True:
     print('------------------')
     print('Enter 1 to check balance \nEnter 2 to send money \nEnter 0 to logout')
     todo_next = int(input('\nChoose Option: '))
     if todo_next == 1:
      print(f'Account Balance: {user["balance"]}')
     elif todo_next == 2:
       send_to = input('Enter the account number to send to: ')
       if len(send_to) != 10:
        print("Invalid Account number(account number should be 10-digit long)")
       else:
        for x in db:
         if x['account_number'] == send_to:
           send_amount = int(input('\nEnter amount to send: '))
           if send_amount <= user['balance']:
            print(f"Confirm Receiver's details \nAccount Number: {send_to}  \nAmount: {send_amount}" )
            confirm = int(input('Enter 1 to confirm transaction or 0 to cancel: '))
            if confirm == 1:
             user['balance'] -= send_amount
             x['balance'] += send_amount 
             print(f'You have sent {send_amount} to this account: {send_to} ')
            else:
             print("Cancelled")
           else:
            print("Insufficient balance")
           print(x)
           continue
        else:
          print("Account number does not exist")
       
     elif todo_next == 0:
      break 
     else:
       print('Invalid Option picked(pick 1 or 2 or 0)')
       continue
    print(db)
 else:
   print('Invalid input')
