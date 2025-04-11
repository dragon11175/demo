def smartATM():
    currect_pin=8059
    print("WELCOME TO SMART_ATM\n")
    print("ENTER YOUR PIN CODE: ")
    pin=int(input("ENTER YOUR PIN CODE"))

    if pin==currect_pin:
        print("1.check balance:\n2.deposite\n3.withdraw\n4.exit\n")
        choice=int(input("ENTER YOUR OPTION:"))

    else:
        print("INVALID PIN!")


    

smartATM()    