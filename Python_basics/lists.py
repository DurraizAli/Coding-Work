# Copyrights reserved to Durraiz Ali
# Contact me at 👉 durraizbukhari1234@gmail.com
#  Pyhton Lists
#             Use to store multiple values in a single variable
# -> Lists are ordered means new entry will be added in the end
# -> Allow Duplicates
# -> Lists are changeable means that items can be removed, add or changed
mylist = ["apple","banana","cherry"]
print(mylist[2])

# List length
print(len(mylist))

# List datatypes
#           List can contain different data types
list1 = ["abc", 34, True, 40, "male"]
print(type(mylist))

# We can also use list constructor to make list
thislist = list(("apple", "banana", "cherry"))
 # note the double round-brackets
print(thislist)
# Check if Item exist in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Changing the item info in list using the index
thislist[1]="Blackberry"
print(thislist)
# We can also put values in between and they can be multiple
thislist[1:2] = ["banana","strawberry"] # put these values in between 0 and 1 index
print(thislist)

# Insert()
#        Insert command is used to add new items at the end of list or in specific location
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Loop through list

for x in thislist:
  print(x)

# List Comprehension
    #           newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


