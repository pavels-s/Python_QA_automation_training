data = input("Enter your number : ")
data = int(data)

if (data == 0):
    print("Number is zero")
elif (data % 2 == 0) and (data > 0):
    print("This is positive Even number")
elif (data % 2 == 0) and (data < 0):
    print("This is negative Even number")
else:
    print("This is Odd number")

print("Extra line of the end of Condition")