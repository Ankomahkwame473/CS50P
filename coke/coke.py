amountdue = 50
while True:
    print(f"Amount Due: {amountdue}")
    coinvalue = int(input("Insert Coin: "))
    if coinvalue == 25 or coinvalue == 10 or coinvalue == 5:
        amountdue -= coinvalue
        if amountdue <= 0:
            print(f"Change owed: {abs(amountdue)}")
            break

