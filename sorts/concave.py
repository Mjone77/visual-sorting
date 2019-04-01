import math
import random
from config import config
import helpers

""" A sorting alg of my design which sorts by comparing opposite elements of the list
    Input: List to sort
    Output: Dictionary of the sorted_list, comparisons, and accesses"""
def concave_sort (nums):
    nums_length = len(nums)
    # Append a new element if an odd number exists to avoid excluding an element from the comparisons
    odd = nums_length%2 != 0
    if odd:
        nums.append(0)
        nums_length+=1
    if config('VERBOSE'):
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
                helpers.swap(nums, i, o_i)
                access+=4
            comps+=1
            access+=2
    # Recursion
    if nums_length > 3:
        if config('VERBOSE'):
            print(str(cid)+" | Bal "+str(nums))
            print(str(cid)+" | Is balanced? "+str(helpers.is_balanced(nums)))
        left_sorted = concave_sort(nums[:half_size])
        right_sorted = concave_sort(nums[half_size:])
        sorted_list = left_sorted['sorted_list'] + right_sorted['sorted_list']
        comps += left_sorted['comparisons'] + right_sorted['comparisons']
        access  += left_sorted['accesses'] + right_sorted['accesses']
    else:
        sorted_list = nums
    if odd:
        sorted_list.remove(0)
    if config('VERBOSE'):
        print(str(cid)+" | Out "+str(sorted_list))
    return {"sorted_list": sorted_list, "comparisons": comps, "accesses": access}