import random
import math

""" Shuffles a given list by randomly changing the index of elements
    Input: list to be shuffled
    Output: A shuffled list
"""
def shuffle_list (nums):
    max_i = len(nums) - 1
    for i, value in enumerate(nums):
        new_i = random.randint(0, max_i)
        other_value = nums[new_i]
        nums[new_i] = value
        nums[i] = other_value
    return nums

""" Returns a list filled with independentally generated random ints """
def get_rand_list (size, min_val, max_val):
    nums = []
    for i in range(size):
        nums.append(random.randint(min_val, max_val))
    return nums

""" Returns a list of the given size whose elements have values equal to their index """
def get_orderd_list (size):
    nums = []
    for i in range(size):
        nums.append(i)
    return nums

""" Returns a shuffled ordered list. Useful to generate randomly ordered lists with unique elements """
def get_shuffled_list (size):
    return shuffle_list(get_orderd_list(size))

""" Verifies that a list is properly sorted """
def is_sorted (nums):
    return nums == sorted(nums)

""" Verifies that a list is balanced (all values in the left half are < all values in the right half) """
def is_balanced (nums):
    half_size = int(math.floor(len(nums)/2))
    return sorted(nums[:half_size])[-1] < sorted(nums[half_size:])[0]