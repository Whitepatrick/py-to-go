target_length = 6
#num_range = xrange(100, 1000)
num_range = xrange(100000, 1000000)
slayer_nums = []

def pop_append_join(value):
    val_array = [int(i) for i in str(value)]
    popped_val = val_array.pop(0)
    val_array.append(popped_val)
    return int(''.join(map(str,val_array)))

def add_and_arrange(value):
    total = value + value + value
    return total

for i in num_range:
    pop = pop_append_join(i)
    if pop == i*3:
        slayer_nums.append(i)
    else:
        print "nope %d" % i

print ""
print ""
print slayer_nums
print ""
print ""
