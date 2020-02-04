"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded\
message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be\
decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example,\
'001' is not allowed.

"""


def helper(message, k, memo):
    if k == 0:
        return 1
    s = len(message) - k
    if message[s] == '0':
        return 0
    if memo[k] is not None:
        return memo[k]
    result = helper(message, k - 1, memo)
    if k >= 2 and int(message[s:s + 2]) <= 26:
        result += helper(message, k - 2, memo)
    memo[k] = result
    return result


def num_ways(message):
    memo = [None] * (len(message) + 1)
    return helper(message, len(message), memo)
