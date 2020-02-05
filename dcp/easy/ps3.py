"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

"""


class LogDataStructure:
    def __init__(self, n):
        self.current_index = 0
        self.max_size = n
        self.log = [None] * self.max_size

    def record(self, order_id):
        # O(1)
        self.log[self.current_index] = order_id
        self.current_index = (self.current_index + 1) % self.max_size

    def get_last(self, i):
        # O(1)
        return self.log[i - 1]


lds = LogDataStructure(5)
lds.record(100)
lds.record(101)
lds.record(102)
lds.record(103)
print(lds.get_last(1))  # 100
lds.record(104)
lds.record(105)
print(lds.get_last(1))  # 105
print(lds.get_last(5))  # 104
