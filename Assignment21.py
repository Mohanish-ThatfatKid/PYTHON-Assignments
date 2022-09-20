# 1. Write a recursive python function to print first N natural numbers.

def natural_numbers(n):
    if n > 0:
        natural_numbers(n-1)
        print(n, end=" ")


n = int(input("Enter a numer:"))
natural_numbers(n)


# 2. Write a recursive python function to print first N natural numbers in reverse order
def revrs_natural(n):

    if n > 0:
        print(n, end=" ")
        revrs_natural(n - 1)


n = int(input("Enter number:"))
revrs_natural(n)

# 3. Write a recursive python function to print first N odd natural numbers
def odd_natural(n):

    if n>0:
        odd_natural(n-1)
        if n % 2 != 0:
            print(n, end=" ")


s = int(input("Enter a NUmber:"))
odd_natural(s*2)


# 4. Write a recursive python function to print first N odd natural numbers in reverse order
def rev_odd_natural(n):
    if n % 2 != 0:
        print(n, end=" ")
    if n > 0:
        rev_odd_natural(n - 1)


s = int(input("Enter a NUmber:"))
rev_odd_natural(s*2)

# 5. Write a recursive python function to print first N even natural numbers.
def even_natural(n):

    if n>1:
        even_natural(n-1)
        if n % 2 == 0:
            print(n, end=" ")


s = int(input("Enter a NUmber:"))
even_natural(s*2)


# 6. Write a recursive python function to print first N even natural numbers in reverse order.
def rev_even_natural(n):
    if n % 2 == 0:
        print(n, end=" ")
    if n > 1:
        rev_even_natural(n - 1)


s = int(input("Enter a Number:"))
rev_even_natural(s*2)

# 7. Write a recursive python function to print squares of first N natural numbers
def natural_squares(n):
    if n > 1:
        natural_squares(n - 1)
        print(n**2,end=" ")


s = int(input("Enter a Number:"))
natural_squares(s)

# 8. Write a recursive python function to print cubes of first N natural numbers
def natural_cube(n):
    if n > 1:
        natural_cube(n - 1)
        print(n**3,end=" ")


s = int(input("Enter a Number:"))
natural_cube(s)

# 9. Write a recursive python function to print first N multiples of a given number.
def multiples(n):
    if n == 1:
        return 1
    s = n*multiples(n-1)
    return s


s = int(input("Enter a Number:"))
print(multiples(s))

# 10. Write a recursive python function to print a number in reverse order.
def reverse(n, r):
    if n == 0:
        return r
    else:
        return reverse(n//10, r*10 + n % 10)


number = int(input("Enter number: "))

reversed_number = reverse(number, 0)

print("Reverse of {} is {}" .format(number, reversed_number))


