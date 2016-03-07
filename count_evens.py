num_array = [1,2,3,4,5,6,7,8,9,10,11]
def count_evens(nums):
    even_amt = []
    for counter, number in enumerate(nums):
        if number % 2 == 0:
            even_amt.append(number)
    return len(even_amt)

ce = count_evens(num_array)
print ce
