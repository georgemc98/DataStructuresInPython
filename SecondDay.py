# def __init__(self, paraone,paratwo) is the format
# def method(self, paraone) - self is always first parameter

# use O(n) to approximate the running time of the dominant term
# order of magnitude function describes the part of T(n) that increases the fastest as n increases
# it provides useful approximation of number of steps in computation
# for T(N) = 5n^2 and 27 n and 100 we say O(n^2)



def anagram(s1,s2):
    a_list = list(s2)
    pos1=0
    bool = True
    while pos1<len(s1) and bool:
        pos2 =0
        found = false
        while pos2<len(a_list) and not found:
            if s1[pos1]== a_list[pos2]:
                found= True
            else:
                pos2 = pos2 + 1
 

