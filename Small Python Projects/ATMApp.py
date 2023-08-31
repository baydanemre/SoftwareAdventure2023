amountinbank = 10000
print("WELCOME TO MY ATM")
print("Deposit : 1")
print("Withdraw : 2")
print("Your Amount: 3")
print("Exit : 4")

selection = input("Please Enter a number: ")

if(selection == "1"):
    amountDeposited = int(input("Enter the amount: "))
    amountinbank += amountDeposited
    print("Your new amount: ",amountinbank)

elif(selection == "2"):
    amountWithdrawed = int(input("Enter the amount: "))
    if(amountWithdrawed > amountinbank):
        print("Transaction is invalid")
    else:
        amountinbank -= amountWithdrawed
        print("Your new amount: ",amountinbank)

elif(selection == "3"):
    print("Your amount:",amountinbank)

elif(selection == "4"):
    print("Exited.")

else:
    print("Enter a valid transaction")


