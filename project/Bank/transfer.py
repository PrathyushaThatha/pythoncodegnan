#transfer function defination
def transfer(sender:int,receiver:int,transfer_amount:int):
    if receiver in users:
        curr_amount=users[sender]["balance"]
        if curr_amount>=transfer_amount:
            users[sender]["balance"]-=transfer_amount
            users[receiver]["balance"]+=transfer_amount
            return f"{transfer_amount} transfer successful and current balance is{users[sender]['balance']}"
        return "Insuficient balance"
    return "Receiver amount not found"
