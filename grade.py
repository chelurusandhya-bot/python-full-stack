a = int(input("Enter marks of sub1:"))
b = int(input("Enter marks of sub1:"))
c = int(input("Enter marks of sub1:"))
d = int(input("Enter marks of sub1:"))
e = int(input("Enter marks of sub1:"))
 
Total = a+b+c+d+e
avg = (a+b+c+d+e)//5

print("Total:",Total)
print("Average:",avg)

if avg>=90:
    print("Grade: A")
elif avg>=75:
    print("Grade: B")
elif avg>=60:
    print("Grade: C")
elif avg>=50:
    print("Grade: D")
else:
    print("Grade: F(Fail)")
    