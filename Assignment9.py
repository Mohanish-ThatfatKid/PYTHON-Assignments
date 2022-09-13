# 1. Write a python script to print MySirG N times on the screen
n = int(input("Enter Number How many times you want to print msg: "))
i = 0
while i < n:
    print("MySirG")
    i += 1

# 2. Write a python script to print first N natural numbers
n = int(input("Enter how many Natural numbers you want to print: "))
i = 1
while i <= n:
    print(i," ", end="")
    i += 1
print()

# 3. Write a python script to print first N natural numbers in reverse order
n = int(input("Enter how many Natural numbers you want to print in reverse: "))
i = n
while i > 0:
    print(i," ", end="")
    i -= 1
print()

# 4. Write a python script to print first N odd natural numbers
n = int(input("Enter how many odd Natural numbers you want to print: "))
i = 0
while i <= n*2:
    if i % 2 != 0:
        print(i, " ", end="")
    i += 1
print()

# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter how many odd Natural numbers you want to print in reverse: "))
i = n*2
while i > 0:
    if i % 2 != 0:
        print(i, " ", end="")
    i -= 1
print()

# 6. Write a python script to print first N even natural numbers
n = int(input("Enter how many even Natural numbers you want to print: "))
i = 1
while i <= 10:
    print(i*2, " ", end="")
    i += 1
print()

# 7. Write a python script to print first N even natural numbers in reverse order
n = int(input("Enter how many even Natural numbers you want to print in reverse: "))
i = n*2
while i > 0:
    if i % 2 == 0:
        print(i, " ", end="")
    i -= 1
print()

# 8. Write a python script to print squares of first N natural numbers
n = int(input("Enter Natural numbers to get Squares: "))
i = 1
while i <= n:
    print(i**2, " ", end="")
    i += 1
print()

# 9. Write a python script to print cubes of first N natural numbers
n = int(input("Enter Natural numbers to get Cubes: "))
i = 1
while i <= n:
    print(i**3, " ", end="")
    i += 1
print()

# 10. Write a python script to print first 10 multiples of N

n = int(input("Enter Number you want to multiply to first 10 numbers : "))
i = 1
while i <= 10:
    print(i*n, " ", end=" ")
    i += 1
print()



