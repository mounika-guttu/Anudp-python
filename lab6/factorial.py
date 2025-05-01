n=int(input("enter a number for factorial:"))
fact=1
while n>0:
    fact=fact*n
    n-=1
print("factorial of the number is:",fact)