### Nested List Exercise Summary:
NWEA Candidate: Dennis Tanaruno - Nested List Code Sample request exercise.

### Code Sample Request:
Coding exercise: Given a nested list of integers, implement a function to flatten it. Each element is either an integer, or a list -- whose elements may also be integers or other lists. Provide a github gist link to your code and tests,. You may use whatever language you are comfortable with but do not use any built-in flattening functions that provide this functionality like Ruby’s Array.flatten.

### Test Cases and Results:
- tc1 = [[1,1],2,[1,1]]
  - output1 = [1,1,2,1,1]
- tc2 = [1,[4,[6]]]
  - output2 = [1,4,6]
- tc3 = [1, [4, [6]]]
  - output3 = [1, 4, 6, 2, 5]
- tc4 = [[1,[4,[6, [2],[5]]]]]
  - output4 = [1, 4, 6, 2, 5]

### Approach:
The Approach implemented for this solution is to intuitively check if each item is a list or an integer. The first part will be to create the flatten list function append the integers to an empty list after checking if the nested list is empty or contains an item.

A function that the constructor can call to make a flattened list.
ret_next() and chk_next() methods that iterate over a plain list, by keeping track of the current position within it.
The first part is best done with recursion 

### Built with:
- [python](https://www.python.org/)
