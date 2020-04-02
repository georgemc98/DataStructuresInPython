import math

# control structures - for loops
# data types - ints, strings
#
# Abstract data type is a logical description of how we view data and operations wo their implementation
# Data structure is the implementation of ADT- provides a physical view of the data using collection of constructs and data types
# This provides implementation-independent view of data, can change data structure without changing interaction between user and ADT
#

# java and python and both object oriented - but class is optional in Python
# python is more flexible and are maintained dynamically
# python is interpreted, java is compiled, python takes double the time java does to implement

def read_file(fileName):
    with open(fileName, "r")as in_file:
        for line in in_file:
            print(line)

# int and float allow operations: +-*/**(exponentation), int allows % and // for int division
# bool is true or false, operators are and, or, not, < > <= >= !=

x = 10
x = "csci 356"
print(x)

sum:int =0
# int_list: list [int] = [1, 2, 3]
# returns integer with string input

#  lists, strings and tuples use these operations
# [x] index at x, [-x] index behind x, x+y combine x and y, x*y repeat x, y times, x in y whether x is in y or not
# len(x) finds length of element, [x:y] extact elements from position x to y

# def string_to_int(string:str) -> int:
collect = [1, 2, 3, 4, 5]

print(collect[1:3])

collect.insert(1, 3)
y = collect.pop()
q = collect.pop(1)
# y is assigned 5 and removed
# q is assigned 2 and removed
# append adds items to end of list - .append(element)
# insert adds item in position - .insert(element, index)
# pop removes and returns last item, pop(i) remove and returns item to index i of list

# .sort() sorts all the items in a list
# .reverse reverses all the items in a list
# del collect[i] will delete element in position i and del collect [2:5] deletes range
# .index(item) returns index of first occurence of item
# .count(item) returns numbers of occurences of items
# .remove(item) will remove the first occurence of an item

# range represent a sequence of numbers
# list(range(x)) generates a list of ints ranging from o to x-1
# list(range(x,y)) generate list of ints from x to y-1
# lsit(range(x,y,z)) generates a list of ints ranging from x to y-1 with an incrementor of z
# list(range(4,1,-2) - start at 4 and subtract 2, start at 2 subtract 2, it is below 1 so theres only (4,2) in the list
# string.center(w) returns the string centered around w
# string.lower() returns a string with all letters in a string to lower case
# string.upper() returns a string with all letters uppercase
# string.find(item) returns index of first occurence of item
# string.split(char) splits into list of substrings at char


phrase = "this is an example"
phrase.split()
print(phrase)

# strings are immuntable, lists are mutable
exList = [1, 2, 3, 4]
exString = "1,2,3,4"
exList[1] = 3
# exString[1] = '3' is not possible

# tuples are written like (StudentA, 194858, True)
# immutable like a string

# set type uses {} instead of [] {StudentA, 395750294, True}, set() for an empty set

# x.in(set): return whether x is in set
# len(set): returns cardinality of set
# set1 | set 2 returns with all elements in set one and two
# set1 & set2 returns with only common elements
# set1 -set2 returns a set with all set 1 elements that aren't in set2
# set1<= set2 whether all items of set 1 are in set2
# set1.union(set2) changes set1 to list with all items in sets
# set1.intersection(set2) changes set1 to common lists
# set.clear() removes all items

# tuples are written as key:value {"united states":"Washington","France":"Paris","China":"Beijing}
# pairs have no particular order
# my_dict["France"] would return paris
# key in my_dict: returns True is key is in my_dict
# del my_dict[key] removes pair associated with my_dict
# my_dict.keys() - returns key, my_dict.values() returns the values, my_dict.item() returns object
# my_dict.get(key): returns values associated with key, my_dict.get(key,alt): return value associated with key, alt otherwise

user_name = input("Please enter your name: ")
radius = float(input ("enter the radius of the circle"))

# print can take multiple parameters
print("hello", "world", sep="!")
print("hello", "world", end="!\n")

# print("%s is %d years old." % (name, age)) is a formatted string print, %s is string and %d is a double
# %d, %i for integer, %u is unsigned int (positive only), %f is for floats, %c for char, %s for string %% for modulus

f =1
while f<=5:
    print("f=", f)
    f = f+1

for i in [1, 5, 6, 9, 11, 3]:
    print(i)

for j in range(4):
    print(j**2)


word_list = ["cat", "dog", "rabbit"]
letter_list = []

for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)

price = 300

if price >= 500:
    print("It is too expensive")
elif price>= 100:
    print("It is a normal price")
else:
    print("Cheap")

# not a good switch case
priority_desc = {0:"High", 1:"Medium", 2:"low"}
description = priority_desc.get(2,"invalid")

def square_root(n):
    if n<0:
        n = abs(n)
    return math.sqrt(n)


print(square_root(9))

def newtonsMethod(n, guessRound=20):
    root = n / 2
    for k in range(guessRound):
        root = .5*(root + n/root)
    return root

