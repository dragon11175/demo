def smartATM():
    currect_pin=8059
    current_balance=5000
    print("\n\n!WELCOME TO SMART_ATM!\n")
    pin=int(input("ENTER YOUR PIN CODE:"))

    if pin==currect_pin:
        print("1.check balance:\n2.deposite\n3.withdraw\n4.exit\n")
        choice=int(input("ENTER YOUR OPTION:"))
        if choice==1:
            print("YOUR CURRENT BALANCE NOW:",current_balance)

        elif choice==2:
            deposite=int(input("ENTER HOW MUCH MONEY YOU WANT DEPOSITE:"))
            if deposite<=0:
                print("INVALID AMMOUNT")
            else:
                current_balance=current_balance+deposite
                print(f"SUCCESFULL!\n\nyour current balance is now:{current_balance}")

        elif choice==3:
            withdraw=int(input("ENTER YOUR WITHDRAW AMMOUNT:"))
            if withdraw<=0 and withdraw>current_balance:
                print("PLEASE ENTER VALID AMMOUNT")
            else:
                current_balance=current_balance-withdraw
                print("YOUR WITHDRAW SUCCESSFULL!",current_balance)
        
        elif choice==4:
            print("GOOD BYE !\nHAVE YOUE A GOOD DAY!")

    else:
        print("INVALID PIN!")


smartATM()    