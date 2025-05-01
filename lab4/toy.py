code = int(input("Enter toy code (1-Battery, 2-Key, 3-Electrical): "))
amount = float(input("Enter amount: "))

if code == 1 and amount > 1000:
    amount *= 0.9
elif code == 2 and amount > 100:
    amount *= 0.95
elif code == 3 and amount > 500:
    amount *= 0.9

print("Payable amount:", amount)
