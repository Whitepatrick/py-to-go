#For what six-digit number SLAYER is the following equation true, where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS

target_length = 6


def get_inuput():
    value = input("Enter a 6 digit number:\n")
    return value

while True:
    try:
        value = int(get_inuput)
        break
    except (ValueError, TypeError, NameError):
        continue
    break

if len(str(value)) > target_length:
    print "%d is too many digits" % value
elif len(str(value)) < target_length:
    print "%d isn't enough digits" % value
else:
    next

def bookend_values(value):
    val_array = [int(i) for i in str(value)]
    bookends = (val_array[0], val_array[-1])
    return bookends

def add_and_arrange(value):
    total = value + value + value
    return total

bv = bookend_values(value)
add = add_and_arrange(value)

if bv != bookend_values(add):
    print bv, bookend_values(add)
    print "these don't match"
else:
    print bv, bookend_values(add)
    print "these match"
