target_length = 6
num_range = xrange(100000, 1000000)
slayer_nums = []

def get_inuput():
    value = input("Enter a 6 digit number:\n")
    return value

def check_len(value):
    if len(str(value)) > target_length:
        print "%d is too many digits" % value
    elif len(str(value)) < target_length:
        print "%d isn't enough digits" % value
    else:
        return value

def pop_and_append(value):
    val_array = [int(i) for i in str(value)]
    pop_val = val_array.pop(0)
    

def bookend_values(value):
    val_array = [int(i) for i in str(value)]
    bookends = (val_array[0], val_array[-1])
    return bookends

def add_and_arrange(value):
    total = value + value + value
    return total

for i in num_range:
    bv = bookend_values(i)
    add = bookend_values(add_and_arrange(i))
    if bv == reversed(add):
        slayer_nums.append(i)
    else:
        print "%d won't work" % i
        print add
        print bv

print slayer_nums
