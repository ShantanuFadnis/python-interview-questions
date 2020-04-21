"""
Determine whether the given two strings are Anagram or not. 
"""

def O_of_n(index:int):
    str1 = "silent"
    str2 = "listen"
    if len(str1) == len(str2):
        l1 = []
        for ch in str1:
            index = int(ch)
            l1[index] += 1

        for ch in str2:
            index = int(ch)
            l1[index] -= 1

        if len(l1) == 0:
            print("It is a Anagram.")
        else: print("It is not an Anagram.")
    else:
        print("It is not an Anagram.")

def O_of_1():
    l1 = "silent"
    l2 = "listen" 
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("It is not an Anagram.")
    else:
        print("It is not an Anagram.")

if __name__ == "__main__":
    n = 0
    O_of_n(n)
    O_of_1() 
    