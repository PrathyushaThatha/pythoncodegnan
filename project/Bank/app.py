#user table
users={
    1234: {"name":"prathyusha","email":"prathyushathatha@gmail.com","balance":10000,"password":"1234"},
    1235: {"name":"pravalika","email":"pravalikathatha@gmail.com","balance":50000,"password":"1235"}
    }

#services
def register(name:str,email:str,initial_deposite,password:str):
    pass

#login
def login(account:int,password:str)->bool:
    if account in users:
        if password==users[account]["password"]:
            return True 
        return False
    return False

#balance functon defination
def balance(account:int)->int:
    curr_amount=users[account]["balance"]
    return curr_amount

#withdraw function defination
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount=users[account]["balance"]
    if curr_amount>=withdraw_amount:
     users[account]["balance"]-=withdraw_amount
     return f"{withdraw_amount} withdraw successful and current balance is{users[account]['balance']}" 
    return "insufficient balance"  

#deposite fuction defination
def deposite(account:int,deposite_amount:int):
    curr_amount=users[account]['balance']
    
    users[account]['balance']+=deposite_amount
    return f"{deposite_amount} deposite successful and current balance is{users[account]['balance']}" 
    return "insufficient balance"
    

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


#ministatement function defination
def ministatement(account:int):
    print("your in ministatement page")

#logout function defination
def logout():
    return "Thank you using small scale bank service,Byee....."

#main function
if __name__ == "__main__":
    print("welcome to the small scale bank")
    print("1.register \n 2.login")
    choice=int(input("Select your option"))
    #calling register function
    if(choice==1):
        print("Registration under development process....")
    #calling login function
    elif(choice==2):
        account=int(input("enter your account number:"))
        password=input("enter your password:")
        login_val=login(account=account,password=password)
        while login_val:
            print("The small scale bank providing services")
            print("1.balance \n 2.withdraw \n 3.deposite \n 4.transfer \n 5.ministatement \n 6.logout")
            choice=int(input("enter your choice(1-6):"))
            if choice==1:
                #call balance function
                current_balance=balance(account=account)
                print(f"current balance is:{current_balance}")
            elif choice==2:
                amount=int(input("enter your withdraw amount:"))
                #call withdraw function
                res=withdraw(account=account,withdraw_amount=account)
                print(res)
            elif choice == 3:
                amount = int(input("Enter deposit amount: "))
                # call deposit function
                res = deposite(account=account, deposite_amount=amount)
                print(res)

            elif choice == 4:
                receiver = int(input("Enter receiver account number: "))
                amount = int(input("Enter transfer amount: "))
                # call transfer function
                res = transfer(
                    sender=account,
                    receiver=receiver,
                    transfer_amount=amount
                )
                print(res)

            elif choice == 5:
                # call mini statement function
                res = ministatement(account=account)
                print(res)

            elif choice == 6:
                # call logout function
                logout()
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 6.")

    else:
        print("Invalid option! Please select either 1 or 2.")