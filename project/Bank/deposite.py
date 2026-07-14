#deposite fuction defination
def deposite(account:int,deposite_amount:int):
    curr_amount=users[account]['balance']
    
    users[account]['balance']+=deposite_amount
    return f"{deposite_amount} deposite successful and current balance is{users[account]['balance']}" 
    return "insufficient balance"
