#Check whether a year is a leap year. 

y = int(input("enter the year : "))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):

    print(y, "is Leap year") 
else:
    print(y, "is Not a leap year")



#Count positive, negative and zero values in a list. 

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive values:", positive)
print("Negative values:", negative)
print("Zero values:", zero)



# Validate whether entered marks lie between 0 and 100. 

marks = float(input("Enter marks: "))

if marks >= 0 and marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")



# palindrome checking

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
