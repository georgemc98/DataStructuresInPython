import timeit
import random



from timeit import Timer


def anagram_solution4(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] +1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] +1

    j=0
    still_ok = True
    while j<26 and still_ok:
        if c1[j]==c2[j]:
            j=j+1
        else:
            still_ok =False
    return still_ok


print(anagram_solution4("python","ythonp"))


# 2n + 26 is linear solution because there are two for loops and 26 iterations in the while loop

# two commmon operations are idexing and assigning to an index position
# if it takes the same amount of time no matter how much data, O(1)
# to grow a list, you can append method or concatenate operator, concatenate by O(k) where k is size of list

# def test1 uses concatenation
# def test2 uses append
# def test3 uses list comprehension
# def test4 uses range

# call function you want to test
# t1 = Timer("test1()", "from __main__import test1")
# print("concat ", t1.timeit(number=1000), "milliseconds")

# pop on list end O(1) but on list front or aywhere else is O(n)

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    print(t)

# stack is last in first out, the end is the top and beginning is the tail
# stack adt is defined by the following operations
# Stack() - takes no parameters, creates a new stack
# push(item) adds item to the top of the stack
# pop() returns and removes items from stack top
# peek() returns item at stack top but doesn't remove
# is_empty() returns whether stack is empty or not
# size() shows size of stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

#   def push(self, item):
#       self.items.append(0,item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())

s.push(6)
s.push("cat")
print(s.peek())
s.push(True)

print(s.size())
print(s.isEmpty)
s.push(8.4)

# stacks are useful to solve real problems
# processing of language constructs, simple balance paranetheses and balanced symbols
# convert decimal numbers to binary
# convert infix expression to prefix and postfix expressions and
# balances parentheses ask each opening symbol has according xlosing symbols and all parentheses are properly nested
# if symbol is open parenthesis, push it on stack
# if symbol is close, pop stack
# as long as pop and push are equal, equation is balanced
# balacned symbols problem is a more general situation arising in many programming languages
#

def par_checker(symbol_string):
    s=Stack()
    balanced = True
    index =0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index +1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(par_checker("()"))