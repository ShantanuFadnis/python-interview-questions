"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


def find_sum(my_list, k):
    my_list.sort()
    fi = 0
    li = -1
    first = my_list[fi]
    last = my_list[li]
    for _ in range(len(my_list)):
        diff = k - first
        if fi >= len(my_list) + li:
            return False
        if diff == last:
            return True
        if last > diff:
            li -= 1
            last = my_list[li]
        elif last < diff:
            fi += 1
            first = my_list[fi]
    return False
