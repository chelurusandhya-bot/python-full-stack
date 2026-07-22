actualamount = int(input("Enter a number"))
removeamount = int(input("Enter a number"))
if removeamount <= actualamount:
    availablebalance = actualamount - removeamount
    print("Available balance:", availablebalance)
else:
    print("Insufficient balance")