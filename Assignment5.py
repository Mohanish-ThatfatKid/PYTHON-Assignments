# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)

num = int(input("Enter A number: "))
print(int(num/10))

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
print(int(num % 10))

# 3. Write a python script to swap data of two variables
number1 = 2456
number2 = 5678
number1, number2 = number2, number1
print(number1, number2)

# 4. Write a python script to find x power y, where values of x and y are given by user
numx = int(input("Enter a Number: "))
numy = int(input("Enter Power Number: "))
print(numx**numy)

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.

num_3digit = int(input("Enter any 3-Digit number: "))
print(int(num_3digit/100))


# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.

print(int((num_3digit/10) % 10))

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.

print(int(num_3digit % 10))

# 8. Write a python script to use IN operator to display the data present in the list
li = [10, 20, 30, 40, 50, 60]

if 10 in li:
    print("present")
else:
    print("Not Present")


# 9. Write a python script to use NOT IN operator to display the data not present in list

if 10 not in li:
    print("Not present")
else:
    print("Present")

# 10. Write a python script to use IS operator to display if both variables are the same object or not?
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]

print(a is b)
print(a == b)
