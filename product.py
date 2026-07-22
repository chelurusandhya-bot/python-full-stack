p = input("product:")
q = int(input("quantity:"))
price = int(input("price:"))
discount = int(input("discount:"))

total = price * q
print("total:",total)

if total > 5000:
    dis = total * (20/100)
else:
    dis = 0
    print("no discount")
print("discount:",discount)

final = total - dis
print("Final amount:", final)

