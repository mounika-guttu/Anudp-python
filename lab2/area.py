s1=int(input("enter first side"))
s2=int(input("enter second side"))
s3=int(input("enter third side"))
S=(s1+s2+s3)/2
area=(S*(S-s1)*(S-s2)*(S-s3))**0.5
print(f"the area of triangle is{area:.2f}")