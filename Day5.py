from QueueADT import Queue
import random
from DequeADT import Deque
# class Printer:
#
#     def __init__(self, ppm):
#         self.page_rate = ppm
#
#         self.current_task = None
#
#         self.time_remaining = 0
#
#     def tick(self):
#         if self.current_task != None:
#             self.time_remaining = self.time_remaining - 1
#         if self.time_remaining <= 0:
#             self.current_task = None
#
#     def busy(self):
#         if self.current_task != None:
#             return True
#         else:
#             return False
#
#     def start_next(self, new_task):
#         self.current_task = new_task
#         self.time_remaining = new_task.get_pages() * 60 / self.page_rate
#
#
# class Task:
#
#     def __init__(self, time):
#         self.timestamp = time
#
#         self.pages = random.randrange(1, 21)
#
#     def get_stamp(self):
#         return self.timestamp
#
#     def get_pages(self):
#         return self.pages
#
#     def wait_time(self, current_time):
#         return current_time - self.timestamp
#
#
# def simulation(num_seconds, pages_per_minute):
#
#     lab_printer = Printer(pages_per_minute)
#
#     print_queue = Queue()
#
#     waiting_times = []
#
#     for current_second in range(num_seconds):
#         if new_print_task():
#             task = Task(current_second)
#
#             print_queue.enqueue(task)
#
#         if (not lab_printer.busy()) and (not print_queue.is_empty()):
#             next_task = print_queue.dequeue()
#
#             waiting_times.append(next_task.wait_time(current_second))
#
#             lab_printer.start_next(next_task)
#
#         lab_printer.tick()
#         average_wait = sum(waiting_times) / len(waiting_times)
#
#     print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))
#
# def new_print_task():
#     num = random.randrange(1, 181)
#     if num == 180:
#         return True
#     else:
#         return False
#
# for i in range(10):
#     simulation(3600,5)


# deque is an ordered collection of items where items can be added and removed at either rear or front
# items remained ordered in collection, provides both capabilities of stack and queue
# add_front(item) adds item to front, add_rear adds it to rar
# remove_front() and remove_rear() returns and removes item
# is_empty returns true or false
# size() returns items in deque

# palindrome is string that reads same forward and backwards





def pal_checker(a_string):
        char_deque = Deque()
        for ch in a_string:
                char_deque.add_rear(ch)
        still_equal = True
        while char_deque.size() > 1 and still_equal:
            first = char_deque.remove_front()
            last = char_deque.remove_rear()
            if first != last:
                still_equal = False
        return still_equal

# list or unordered list is a collection of tems where each items holds an index
# fr simplicity, assume that lists cant contain duplicate items
# append(item) adds to end, index(item) gives you index, remove(item) removes it from list, search(item) returns True or False
# size(), add(item) adds it to a random position, pop() removes that item in list, pop(pos) removes and returns item in pos

class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:



    def __init__(self):
        self.head = None
        self.firstItem = self.head
        self.lastItem = None

    def is_empty(self):
        return self.head == None


    def add(self, item):
        temp = Node(item)

        temp.set_next(self.head)

        self.head = temp

        

    def size(self):
            current = self.head
            count = 0
            while current != None:
                count = count + 1
                print(current.get_data)
                current = current.get_next()
            return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                print(current.get_data)
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def Insert(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        if (temp == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)


myList = UnorderedList()
myList.add(31)
myList.add(85)
myList.add(93)

print(myList.search(25))

myList.size()

# (myList.Insert(100))

# size search and remove are based on linked list traversal
# traversal refers to process of systemically visiting every node
# size method traverses list and counts number of nodes visited


# ordered lists is where items hold a position based on a characteristic
# usually ascending or descending order
class OrderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            print(current.get_data)
            current = current.get_next()
        return count


    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
            return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

list1 = OrderedList()
list1.add(99)
list1.add(90)
list1.add(11)
list1.add(45)
print(list1.is_empty())

print(list1.size())

