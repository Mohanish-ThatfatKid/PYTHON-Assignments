# 1. Write a python program to store all the programming languages known to you using Set.

s = {"java", "c", "c++", "vb.net", "python", "c#"}

# 2. Write a python program to store your own information {name, age, gender, so on..}
s1 = {"Mohanish", 27, "Male", "Thane", "INDIAN"}

# 3. Write a python script to get the data type of Set.
print(type(s))

# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}

thisset = {"Java", "Python", "Django"}
print("Python" in thisset)

# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

thisset = thisset.union(secondset)
print(thisset)

# 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"}
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

thisset.update(mylist)
print(thisset)

# 7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"Python", "Django", "JavaScript", 'SQL'}
thisset.discard('SQL')
print(thisset)

# 8. Write a python program to delete the set completely.

thisset = {"Python", "Django", "JavaScript", 'SQL'}
del thisset

thisset = {"Python", "Django", "JavaScript", 'SQL'}
thisset.clear()

# 9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}

for i in thisset:
    print(i)

# 10. Write a python program to find the maximum and minimum value in a set.

s2 ={10, 30, 50, 80, 3}
print(min(s2))
print(max(s2))













