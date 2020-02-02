"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

my_list = [10, 15, 3, 7, 8, 19, 54, 67, 48, 98]
k = 27


def find_sum(my_list, k):
    my_list.sort()
    fi = 0
    li = -1
    first = my_list[fi]
    last = my_list[li]
    for _ in range(len(my_list)):
        diff = k - first
        if diff == last:
            return True
        if last > diff:
            li -= 1
            last = my_list[li]
        elif last < diff:
            fi += 1
            first = my_list[fi]
        
    return False


if __name__ == '__main__':
    print(find_sum(my_list, k))
