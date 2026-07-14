#main function
if _name_ == "_main_":
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

