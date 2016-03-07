https://wiki.python.org/moin/ProblemSets
https://www.quora.com/Where-can-I-find-basic-python-practice-problems
http://openbookproject.net/pybiblio/practice/


#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0
def count_evens(nums):

#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'
def hello_name(name):

#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
#cigar_party(30, False) → False
#cigar_party(50, False) → True
#cigar_party(70, True) → True
def cigar_party(cigars, is_weekend):

#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'
def string_times(str, n):

#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False
def first_last6(nums):
