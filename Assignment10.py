# 1. Write a python script to print MySirG N times on the screen

n = int(input("Enter how many times you want to print msg: "))
for i in range(n):
    print("MySirG")

# 2. Write a python script to print first N natural numbers
n = int(input("Enter how many Natural number you Want to print: "))
for i in range(n):
    print(i+1)


# 3. Write a python script to print first N natural numbers in reverse order
n = int(input("Enter how many Natural number you Want to print in reverse: "))
for i in range(n):
    print(n-i)


# 4. Write a python script to print first N odd natural numbers
n = int(input("Enter how many odd Natural number you Want to print: "))
for i in range(1, n * 2, 2):
    print(i)


# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter how many odd Natural number you Want to print in reverse: "))
for i in range(n*2, 0, -1):
    if i % 2 != 0:
        print(i)


# 6. Write a python script to print first N even natural numbers
n = int(input("Enter how many even Natural number you Want to print: "))
for i in range((n+1)*2):
    if i % 2 == 0 and i != 0:
        print(i)


# 7. Write a python script to print first N even natural numbers in reverse order
n = int(input("Enter how many even Natural number you Want to print in reverse: "))
for i in range(n*2, 0, -2):
    print(i)

# 8. Write a python script to print squares of first N natural numbers
n = int(input("Enter Number you want to find Square of: "))
for i in range(n):
    print((i+1)**2)

# solution 2
n = int(input("Enter Number you want to find Square of: "))
for i in range(1, n+1):
    print(i**2)


# 9. Write a python script to print cubes of first N natural numbers
n = int(input("Enter Number you want to find cube of: "))
for i in range(1, n+1):
    print(i**3)


# 10. Write a python script to print first 10 multiples of Nq
n = int(input("Enter Number you want to Multiply for first 10 numbers: "))
for i in range(1, 11, 1):
    print(i*n)



