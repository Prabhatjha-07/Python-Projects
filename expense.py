import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

while (True):
    amount = float(input('enter the amount:'))
    category = input('enter the category:')
    description = input('enter the description:')

    expense = {
    'amount': amount,
    'category': category,
    'description': description
}

    expenses.append(expense)
    
    choice = input('do you want to add another expense?: (y/n)')
    if choice == 'n':
        break
with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

for expense in expenses:
    print('-----------------------------')
    print('Amount:' , expense['amount'])
    print('Category:' , expense['category'])
    print('Description:' , expense['description'])
    print( )

    
total = input(' do you want to see the total spending (y/n):')

total_sum = 0 
if total == 'y':
    for expense in expenses:
        total_sum += expense['amount']
        
    print('total spending:' , total_sum)
    
    
# total = sum(expense['amount'] for expense in expenses)
# print(f'Total expenses: {total}')
    

