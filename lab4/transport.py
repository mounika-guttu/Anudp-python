distance = int(input("Enter distance in Km: "))
if distance <= 50:
    charge = distance * 8
elif distance <= 100:
    charge = distance * 10
else:
    charge = distance * 12
print("Total Fare:", charge)
