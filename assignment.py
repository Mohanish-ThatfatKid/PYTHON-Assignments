# 1. Write a Python script to create a list of first N natural numbers.
from typing import List, Union

l = [x for x in range(1,11)]
print(l)


# 2. Write a Python script to create a list of first N odd natural numbers.

l2 = [x for x in range(20) if x % 2 != 0]
print(l2)

# 3. Write a Python script to create a list of first N even natural numbers.

l3 = [x for x in range(1,21) if x%2 == 0]
print(l3)

# 4. Write a Python script to find the greatest number in a given list of numbers.

l4 = [10, 40, 30, 20, 44, 55, 60, 80, 1]
print(max(l4))

# 5. Write a Python script to find the smallest number in a given list of numbers.
print(min(l4))

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.
sum = 0
for x in l4:
    sum = sum+x

print(sum)

# 7. Write a Python script to remove all non int values from a list.
l5 = ["a", "b", 10, 30, 40, 50, "home", "java", "python",70]
l6 = []
for x in l5:
    if type(x) == int:
        l6.append(x)

print(l6)

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
l7 = [10, 20, 20, 30, 30, 30, 30, 40, 50, 55, 56, 55, 30, 20, 10, 40, 60, 70, 80, 70, 60, 80, 90]
n = int(input("Enter Number to check total count of number:"))
print(n, "Has occurred", l7.count(n), "times.")

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

k = int(input("Enter number to check indices of all occurrence:"))
i = 0
while i < len(l7):
    if l7[i] == k:
        print(k, "Occurred at Index", i)
    i = i+1

# 10. Write a python script to sort a list.
print(sorted(l7))

