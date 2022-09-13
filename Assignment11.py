# 1. Write a python script to calculate sum of first N natural numbers
n = int(input("Enter number to find a sum of that many natural numbers: "))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i
print(sum)

# 2. Write a python script to calculate sum of squares of first N natural numbers
n = int(input("Enter number to calculate sum of squares of natural numbers: "))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i**2
print(sum)

# 3. Write a python script to calculate sum of cubes of first N natural numbers
n = int(input("Enter number to calculate sum of cubes of natural numbers: "))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i**3
print(sum)

# 4. Write a python script to calculate sum of first N odd natural numbers
n = int(input("Enter number to calculate sum of odd natural numbers : "))
sum = 0
for i in range(1,n*2,2):
    sum = sum + i
print(sum)


# 5. Write a python script to calculate sum of first N even natural numbers
n = int(input("Enter number to calculate sum of even natural numbers : "))
sum = 0
for i in range(0, n*2, 2):
    print(i," ",end="")
    sum = sum +i
print(sum)

# 6. Write a python script to calculate factorial of a given number
n = int(input("Enter number to calculate factorial of a given number : "))
sum = 1
for i in range(1,n+1):
    sum = sum * i
print(sum)


# 7. Write a python script to count digits in a given number
n = input("Enter a number to count the digits of a number: ")
print("Number Has {} Digits".format(len(n)))

# 8. Write a python script to calculate sum of digits of a given number
n = input("Enter a number to count the sum of digits of a number: ")
sum = 0
for i in n:
    sum = sum + int(i)
print(sum)

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
n = int(input("Enter a number to find a binary representation"))
bi = ""
while True:
    if n >= 1:
        bi = str(n % 2) + bi
        n = n//2
    else:
        break
print("0b",bi)

# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
#n = int(input("Enter a number to find a binary representation"))
n = int(input("Enter a number to find octal representation: "))
oc = ""
while True:
    if n >= 1:
        oc = str(n % 8) + oc
        n = n//8
    else:
        break
print("0o", oc)

