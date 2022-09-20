# 1. Write a python program to create a simple function which prints “MySirG” .
def show():
    print('"MySirG"')


show()


#2. Write a python program to create a function which expects two arguments and print them in the function body.

def dis(a,b):
    print(a,b)


dis(10, 20)

# 3. Write a python program to create a function which expects an unknown number of arguments.


def aver(*a):
    print("average is",sum(a)/len(a))


aver(10,20,30)
aver(10,20,30,40,60,50)


# 4. Write a python program to create a function which expects kwargs arguments.

def foo(*kwargs):
    for i in kwargs:
        print(i)


foo(10, 20, 30, 40, 50, 60)


# 5. Write a python program to create a function which expects a list as an argument.
def func(l):
    print(type(l))
    for i in l:
        print(i)


li = [10,20,30,40,50,60]
func(li)


# 6. Write a python program to create a function that finds a maximum of four numbers.
def maximumnum(*t):
    print(max(t))


maximumnum(10, 30, 220, 40871, 589)


# 7. Write a python program to sum all the numbers in a list.
def sumlist(l):
    sum = 0
    for i in l:
        sum = sum + i

    print(sum)


li = [10, 20, 30]
sumlist(li)

# solution 2


def suml(l):
    print(sum(l))


l = [10, 20, 30]
suml(l)


# 8. Write a python program to multiply all the numbers in a list.
def funmullist(l):
    mul  = 1
    for i in l:
        mul = mul*i
    print(mul)


lis = [10, 20, 30, 40, 50]
funmullist(lis)


# 9. Write a python program to create a function to check whether a number falls in a given range.
def funran(t):
    if t in range(1,35):
        print("Number {} falls in range.".format(t))
    else:
        print("Number {} does not falls in range.".format(t))


funran(int(input("Enter some random number: ")))


# 10. Write a python program to create a function to check whether a given number is even or odd.
def number(a):
    if a != 0 and a%2 == 0:
        print("Number {} is Even.".format(a))
    else:
        print("Number {} is Odd.".format(a))


number(int(input("Enter number to check even or odd: ")))
