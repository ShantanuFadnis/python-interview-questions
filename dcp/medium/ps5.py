"""
Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try pre-processing the dictionary into a more efficient data structure to speed up
queries.

"""


QUERIES = {'dog', 'deer', 'deal', 'cat', 'camel', 'chicken', 'lion', 'caramel'}
PROCESSED_DICT = {}


def pre_process():
    # O(n^2)
    for item in QUERIES:
        for i in range(1, len(item) + 1):
            if item[0:i] in PROCESSED_DICT:
                PROCESSED_DICT[item[0:i]].append(item)
            else:
                PROCESSED_DICT[item[0:i]] = [item]


def search(query_str):
    # O(n)
    res = []
    for item in QUERIES:
        if item.startswith(query_str):
            res.append(item)
    return res


def search_fast(query_str):
    # O(1)
    if query_str in PROCESSED_DICT:
        return PROCESSED_DICT[query_str]
    return []


pre_process()
print(search(input('> ')))
