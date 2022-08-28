# 1. Write a python script to create a String in 3 different possible ways

s = "This is simple String"

l = ["Mohanish", "Rajendra", "Devrukhkar"]
s1 = " ".join(l)
print(s1)

num = 102039
s3 = str(num)
print(s3)
print(type(s3))

# 2. Write a python script to Get the characters from the start to position 5 (Given String“iNeuron” using the slice syntax)
s4 = "iNeuron"
print(s4[:6])

# 3. 3. Write a python script to Get the characters from position 2 to position 5 (Given String # “Hello Learners” using the slice syntax)
s5 = "Hello Learners"
print(s5[2:6])

# 4. Write a python script to demonstrate String Concatenation adding space in between ( # Given Strings a=”Learning” b=”Python” )
a = "Learning"
b = "Python"
print(a + " " + b)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
a = "iNeuron"
print("Total number of characters in String:", len(a))

# 6. Write a python script to reverse a String. (“iNeuron”)

print(a[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.
ss = "This is simple String"
sub = "simple"
if ss.find(sub) >= 0:
    print("Found")
else:
    print("Not Found")

# 8. Write a python script to check if a string contains only numbers.
s = "1020"
if s.isalnum():
    print("Contains only digits")
else:
    print("Contains everything")

# 9. Write a python script to check if a string contains only characters of the alphabet.
if s.isalpha():
    print("Contains only Alphabets")
else:
    print("Not just Alphabets")

# 10. Write a python script to convert an integer to a string.
number = 12345667
s = str(number)
print(s)



