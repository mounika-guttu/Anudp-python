# Conversion factor
km_to_miles = 0.621371

# Input from user
kilometers = float(input("Enter distance in kilometers: "))

# Conversion
miles = kilometers * km_to_miles

# Output
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
