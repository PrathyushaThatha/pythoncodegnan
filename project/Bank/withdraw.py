#withdraw function defination
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount=users[account]["balance"]
    if curr_amount>=withdraw_amount:
     users[account]["balance"]-=withdraw_amount
     return f"{withdraw_amount} withdraw successful and current balance is{users[account]['balance']}" 
    return "insufficient balance"  
