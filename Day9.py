# Merge Sort has big o of (n/2^(2-1)) or (n/2^(3-1))
# overall has performance of nlogn
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)

        quick_sort_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

        temp = a_list[first]

        a_list[first] = a_list[right_mark]

        a_list[right_mark] = temp

        return right_mark

list = [4,7,3,9,6,24,86,35]
quick_sort(list)
print(list)

# seuqential is O(n) for ordered and unordered lists
# binary search of ordred list is O(log n)
# has tables can provide constant time earching, will degrade f collision resolution is necessary
# bubble selection and insertion are O(n^2)

# trees are used in many areas of computer science
# tree DS have root, branches and leaves
# CS trees have root at the top and leaves on the bottom
# binary tree means each node only has two children or less
#

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
       root.insert(2, [new_branch, [], []])

    return root


def get_root_val(root):
    return root[0]

def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]

r = binary_tree("a")

insert_left(r, "d")

insert_left(r, "b")

insert_right(get_left_child(r), "e")

insert_right(r, "c")

insert_left(get_right_child(r), "f")

print(r)


class BinaryTree:

    def __init__(self, root):
        self.key = root

        self.left_child = None

        self.right_child = None

    def insert_left(self, new_node):

        if self.left_child == None:

            self.left_child = BinaryTree(new_node)

        else:

            t = BinaryTree(new_node)

            t.left_child = self.left_child

            self.left_child = t

    def insert_right(self, new_node):

        if self.right_child == None:

            self.right_child = BinaryTree(new_node)

        else:

            t = BinaryTree(new_node)

            t.right_child = self.right_child

            self.right_child = t

    def get_right_child(self):

        return self.right_child

    def get_left_child(self):

        return self.left_child

    def set_root_val(self, obj):

        self.key = obj

    def get_root_val(self):

        return self.key

r = BinaryTree("a")

r.insert_left("b")

r.get_left_child().insert_right("d")

r.insert_right("f")

r.insert_right("c")

r.get_right_child().insert_left("e")

print(r.get_right_child().get_right_child().get_root_val(), \

        r.get_right_child().get_left_child().get_root_val())

# priority queue acts like queue by dequeuing item from front
# logical order is based on priority, not FIFO
# highest priority items are at the ront and low priority are at the back
# list insertion is O(n) and sorting is 0(nlogn)
#  binary heap for priority queue can allow both enqueue and dequeue in O(logn)
# min heap pputs smallest key at front
# max heap puts largest at front
# take advantage of log nature of balanced binary tree to represent heap
# is symetrical besides the last nodes

# complete binary trees have each level, except for bottom level, has the same amount of nodes
# complete binary trees can be rep. in a single list
# parent is at position p. left child is at 2p and right child is at 2p + 1
# given position n in list, its parent is n//2
# heap order property told hold in complete binary tree rep.

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

