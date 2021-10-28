
# Coding exercise: Given a nested list of integers, implement a function to flatten it. Each element is either an
# integer, or a list -- whose elements may also be integers or other lists. Provide a github gist link to your code
# and tests cases


# create NestedIterator object with the flatten_list function to flatten the nested list
class NestedIterator:
    def __init__(self, inputlist):
        def flatten_list(input_list):
            for integers in input_list:
                if type(integers) is int:
                    self.integers.append(integers)
                else:
                    flatten_list(integers)
        self.integers = []
        self.position = -1          # use to initiate pointer.
        flatten_list(inputlist)

    nestedList = [1, [4, [6]]]

    # return next int if chk_next still contains an item
    def ret_next(self) -> int:
        self.position += 1
        return self.integers[self.position]

    # Returns true if the list still contains items, false if not
    def chk_Next(self) -> bool:
        return self.position + 1 < len(self.integers)


# tc1 = [[1,1],2,[1,1]]
# output1 = [1,1,2,1,1]
# tc2 = [1,[4,[6]]]
# output2 = [1,4,6]
# tc3 = [1, [4, [6]]]
# output3 = [1, 4, 6, 2, 5]
# tc4 = [[1,[4,[6, [2],[5]]]]]
# output4 = [1, 4, 6, 2, 5]

nestedList = [[1, [4, [6, [2], [5]]]]]

# instantiated of the NestedIterator object
i, v = NestedIterator(nestedList), []
while i.chk_Next(): v.append(i.ret_next())

# print the result
print(v)