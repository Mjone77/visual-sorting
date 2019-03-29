#!/usr/bin/python3
import random
import math

# Config variables
NUM_ELEMENTS = 50
MIN_ELEMENT_VALUE = 0
MAX_ELEMENT_VALUE = 99999
ORDERED_ARRAY = True
VERBOSE = False

def main ():
    # Construct random array
    if ORDERED_ARRAY:
        nums = get_shuffled_array(NUM_ELEMENTS)
    else:
        nums = get_rand_array(NUM_ELEMENTS, MIN_ELEMENT_VALUE, MAX_ELEMENT_VALUE)
    print("Random Array\n"+str(nums))
    concave_nums = concave_sort(nums)
    print("Concave Sort\nComparisons: "+str(concave_nums['comparisons'])+"\nAccesses: "+str(concave_nums['accesses'])+"\n"+str(concave_nums['sorted_array']))
    print("Is it sorted? "+str(is_sorted(concave_nums['sorted_array'])))
    #print("Is it balanced? "+str(is_balanced(concave_nums['sorted_array'])))

""" A sorting alg of my design which sorts by comparing opposite elements of the array
    Input: Array to sort
    Output: Dictionary of the sorted_array, comparisons, and accesses"""
def concave_sort (nums):
    nums_length = len(nums)
    # Append a new element if an odd number exists to avoid excluding an element from the comparisons
    odd = nums_length%2 != 0
    if odd:
        nums.append(0)
        nums_length+=1
    if VERBOSE:
        cid = random.randint(0,9999)
        print(str(cid)+" | In "+str(nums))
    comps, access, half_size = 0, 0, int(math.floor(nums_length/2))
    # Loop through all possible offsets to ensure all elements are compared
    for offset in range(half_size):
        # Loop through half the elements to compare with the other half
        for i in range(half_size):
            # Get other_index
            o_i = nums_length-i-1-offset
            if o_i < half_size:
                o_i+=half_size
            # If the left value is greater than the right --> swap them
            if (nums[i] > nums[o_i]):
                value = nums[i]
                nums[i] = nums[o_i]
                nums[o_i] = value
                access+=4
            comps+=1
            access+=2
    # Recursion
    if nums_length > 3:
        if VERBOSE:
            print(str(cid)+" | Bal "+str(nums))
            print(str(cid)+" | Is balanced? "+str(is_balanced(nums)))
        left_sorted = concave_sort(nums[:half_size])
        right_sorted = concave_sort(nums[half_size:])
        sorted_array = left_sorted['sorted_array'] + right_sorted['sorted_array']
        comps += left_sorted['comparisons'] + right_sorted['comparisons']
        access  += left_sorted['accesses'] + right_sorted['accesses']
    else:
        sorted_array = nums
    if odd:
        sorted_array.remove(0)
    if VERBOSE:
        print(str(cid)+" | Out "+str(sorted_array))
    return {"sorted_array": sorted_array, "comparisons": comps, "accesses": access}

""" Shuffles a given array by randomly changing the index of elements
    Input: Array to be shuffled
    Output: A shuffled array
"""
def shuffle_array (array):
    max_i = len(array) - 1
    for i, value in enumerate(array):
        new_i = random.randint(0, max_i)
        other_value = array[new_i]
        array[new_i] = value
        array[i] = other_value
    return array

""" Returns an array filled with independentally generated random ints """
def get_rand_array (size, min_val, max_val):
    nums = []
    for i in range(size):
        nums.append(random.randint(min_val, max_val))
    return nums

""" Returns an array of the given size whose elements have values equal to their index """
def get_orderd_array (size):
    nums = []
    for i in range(size):
        nums.append(i)
    return nums

""" Returns a shuffled ordered array. Useful to generate randomly ordered arrays with unique elements """
def get_shuffled_array (size):
    return shuffle_array(get_orderd_array(size))

""" Verifies that a list is properly sorted """
def is_sorted (nums):
    return nums == sorted(nums)

""" Verifies that a list is balanced (all values in the left half are < all values in the right half) """
def is_balanced (nums):
    half_size = int(math.floor(len(nums)/2))
    return sorted(nums[:half_size])[-1] < sorted(nums[half_size:])[0]

if __name__ == '__main__':
    main()