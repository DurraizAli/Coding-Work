x= 8
y= 34.98
# we can print the type of variable using the type function
print(type(x))
print(type(y))

first_name= "Durraiz"
last_name='Ali'

print(type(first_name))# string type
print(type(last_name)) # string type

# Many values to multiple varibles

value1,value2,value3= 'orange','apple','mango'
print(value1)
print(value2)
print(value3)

#unpacking of list into variable
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output formats
 # multiple outputs in single line

print(x,y,z)

#Concatinate the strings
print(x+y+z)# for strings + work as concatination operator but with int it 
#works like add

# multiline string assigned to variable:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Using Quotes inside of Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Python ke paas character datatype nahin hai so it access the string character
# by positions
a1 = "Hello, World!"
print(a1[1]) # will give e

# We can also loop through the strings
for x in "banana":
    print(x)

# The length of string can be find out by:
c= "Hello World"
print(len(c))

# Hum ye bhi check kr saktay hain ke kisi string main koi word exist krta hai?
check= "The best thing in you is self confidence"
print("best" in check)
print("best" not in check)

                # Slicing Strings in Python
slice= "Hello Worlds"
print(slice[0:5]) #[A:B] A is included and B is excluded string will show 0 to 4
print(slice[:5])
print(slice[5:])
# negative Slicing
b = "Hello, World!"
print(b[-5:-2])

#                .lower() uses to make lower case 
#                .upper() uses to make upper case

# Strip()
#           " method uses to strip whitespaces from start to end "
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace()
#           Uses to replace a string with another string

a= "Durraiz"
print(a.replace("D", "Z")) # My name will change to Zurraiz

# split()
#          method returns a list where the text between the specified seperator
#          become the list items
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# If you want to see more fucntions of strings python you can go to this 
# Link 👉 https://www.w3schools.com/python/python_strings_methods.asp

