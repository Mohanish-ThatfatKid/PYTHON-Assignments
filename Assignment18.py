# 1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)
d = dict(name="Mohanish", age=27, gender="Male",state="Maharashtra",pincode=400603)
print(d)


# 2. Write a python program to access the items of a dictionary by referring to its key name.
for i in d:
    print(d[i])


# 3. Write a python program to get a list of the values from a dictionary.
print(d.values())


# 4. Write a python program to change the value of a specific item by referring to its key name.
print(d)
d['age']=28
print(d)


# 5. Write a python program to print all key names in the dictionary, one by one.
for i in d.keys():
    print(i)


# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)

d1 = {'code': {'language': ("java", "Python")}, 'names': {'frontend': ('om', 'arya')}, 'developer': {'backend': ('mohanish', 'rhuta')}}
for i in d1.items():
    print(i)


# 7. Write a python program to create three dictionaries, then create one dictionary that  will contain the other three dictionaries.
di1 = {'name': 'mohanish'}
di2 = {'age': 27}
di3 = {'gender': 'male'}
dicto = {di1, di2, di3}
print(dicto)


# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

dlis = {}
l = ["name", "age", "gender"]
l2 = ["Mohanish", 27, "male"]
i = 0
if len(l) == len(l2):
    while i < len(l):
        dlis[l[i]] = l2[i]
        i += 1
else:
    print("List have different number of elements")
print(dlis)

# 9. Write a python program to merge two python dictionaries into one dictionary.
smp = {101: "mohanish", 102: "Rhuta"}
smp2 = {103: "om", 104: "arya"}
sampl = {}

for k, v in smp.items():
    sampl[k] = v
for k, v in smp2.items():
    sampl[k] = v

print(sampl)

# 10. Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
 'C': 92,
 'Java': 66,
 'Python': 85
 }
print(min(sample_dict.values()))

