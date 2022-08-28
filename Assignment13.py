# question 1 Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list

li = ["java", "Python", "SQL", "C"]


# Question 2 Write a python script to get the data type of a list.

print(type(li))


# question 3 Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]
print(mylist[-1])


# Question 4 Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript","Python"]

l2 = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

#solution 1

for x in l2:
    if x == "SQL":
        l2[l2.index(x)] = "NoSQL"
    elif x == "Reactnative":
        l2[l2.index(x)] = "Flutter"

print(l2)

# Solution 2 when index number in known

l2[1]="NoSQL"
l2[3]="Flutter"

# Question 5 Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]

mylist2 = ["Java", "SQL", "C", "Reactnative"]
mylist2.append("Python")
print(mylist2)


# Question 6 Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

# Solution 1

firstlist = firstlist+secondlist
print(firstlist)

# solution 2

for x in secondlist:
    firstlist.append(x)

print(firstlist)


# Question 7 Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

print()

# Question 8 Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

thislist2 = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

# Solution 1 In Built function
print(sorted(thislist2))

# solution 2 list function
thislist2.sort()
print(thislist2)


# Question 9 Write a Python script to create a list of city names taken from the user.
# solution 1

lis = eval(input("Enter City name in list format: "))
print(lis)

# Question 10 Write a Python script to create a list, where each element of the list is a digit of a
# given number.

test_list = [56, 72, 875, 9, 173]

print("The original list is : " + str(test_list))

K = int(input("Enter some digit:"))

res = [ele for ele in test_list if str(K) in str(ele)]

print("Elements with digit K : " + str(res))
