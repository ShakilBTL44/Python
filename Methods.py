# len() is not the method of the string but can be used to get the length of the string

name = "Iron man"
print(len(name))      #  ans--> 8


# count() method will returns the number of times a specified value occurs in a string.
name = "Captain America"
print(name.count("z"))   # ans--> 0
print(name.count("c"))   # ans--> 1


# title(), lower(), upper() will returns capitalized, lower case and upper case string respectively.
string = "shakil b pendhari"
print(string.title())   # ans--> Shakil B Pendhari
print(string.lower()) # ans--> shakil b pendhari
print(string.upper()) # ans--> SHAKIL B PENDHARI


# istitle(), islower(), isupper() will returns True if the given string is capitalized, lower case and upper case respectively.
string = "shakil b pendhari"
print(string.istitle()) # False
print(string.islower()) # True
print(string.isupper()) # False


# strip() method will remove whitespaces from both side of the string and returns the string.
# rstrip() and lstrip() will remove whitespaces from right and left side respectively.
animal = " tiger    "
print(animal) # tiger with left and right space
print(animal.strip()) # space will have removed
print(animal.rstrip()) # right space will have removed
print(animal.lstrip()) # left space will have removed


# find() method will search the string and returns the index at which they find the specified value
# rfind() will search the string and returns the last index at which they find the specified value
# Note : find() and rfind() will return -1 if they are unable to find the given string.
name = "shakil pendhari"
print(name.find("a"))    # 2
print(name.rfind("a"))   # 12
print(name.find("z"))    # -1


# replace() will replace str1 with str2 from our string and return the updated string
str = "You are good"
print(str.replace("good","best"))  # You are best


# index() method will search the string and returns the index at which they find the specified value, but if they are unable to find the string it will raise an exception.
name = "shakil pendhari"
print(name.index("ha"))  # 1
# print(name.index("z"))   # returns error valueError


# rindex() will search the string and returns the last index at which they find the specified value , but if they are unable to find the string it will raise an exception.
print(name.rindex("ha"))  # 11

# Note : find() and index() are almost same, the only difference is if find() is unable to find the string it will return -1 and if index() is unable to find the string it will raise an exception.


# isalnum() method will return true if all the characters in the string are alphanumeric (i.e either alphabets or numeric).
name = "shakil123"
print(name.isalnum())   # True
# isalpha() and isnumeric() will return true if all the characters in the string are only alphabets and numeric respectively.
# isdecimal() will return true is all the characters in the string are decimal.
# Note : isnuberic() and isdigit() are almost same, you suppose to find the difference as Home work assignment for the string methods.
nameAlphabets = "shakil";
nameNumeric = "123";
print(nameAlphabets.isalpha())   # True
print(nameAlphabets.isnumeric()) # False
print(nameNumeric.isalpha()) # False
print(nameNumeric.isnumeric()) # True
print(nameNumeric.isdecimal()) # True