class Stack1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def divide_by_2(dec_number):
    rem_stack = Stack1()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2
        bin_string = ""
        while not rem_stack.isEmpty():
            bin_string = bin_string +  str(rem_stack.pop())
        return bin_string

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack1()
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
    new_string = ""
    while not rem_stack.isEmpty():
        new_string = new_string +  digits[rem_stack.pop()]
    return new_string


print(divide_by_2(91))
print(base_converter(3,8))
print(base_converter())

# infix expressions ask operators appears between two operands
# to avoid ambiguity, each operator has a precedence level
# * and / have higher precedence than - and +

# a + (b * c) converts to prefix: +a*bc and postfix: abc*+
# assume infix expression is a string of tokens delimited by spaces
# crate empty stack for operators and an empty list for output
# concert input infix string to list by using string method split
# scan token list from left to right, if token is operand, append it to the end of the output list
# push ( on op stack, pop )
# when input expression is processed, we check op_stack if it is empty

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack1()
    postfix_list = []
    token_list = infix_expr.split()
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

print(infix_to_postfix("( A * B ) / C - D + E"))


def postfix_eval(postfix_expr):
    operand_stack = Stack1()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()
def do_math(op, op1, op2):
        if op == "*":
                return op1 * op2
        elif op == "/":
                return op1 / op2
        elif op == "+":
                return op1 + op2
        else:
            return op1 - op2

print(postfix_eval("5 6 /"))


# queue is an ordered collection where items are added at end(rear) and removed at the front
# items are ended at rear and makes it way to front, first in first out
# enqueue(item) adds it to qurue rear
# dequeue() returns and removes front item
# is_empty returns whether empty or not
# size() returns number of items in queue

class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue('hello')

q.enqueue('dog')

q.enqueue(3)

q.dequeue()


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()

a_list = ["giraffe", "elephants", "dog", "puma", "bear"]

print(hot_potato(a_list, 3))
