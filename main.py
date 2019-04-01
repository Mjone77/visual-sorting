#!/usr/bin/python3
import helpers
from config import config
import sorts.sort_controller as sorts

def main ():
    # Construct random list
    if config('ENUM_LIST'):
        NUMS = helpers.get_shuffled_list(config('NUM_ELEMENTS'))
    else:
        NUMS = helpers.get_rand_list(config('NUM_ELEMENTS'), config('MIN_ELEMENT_VALUE'), config('MAX_ELEMENT_VALUE'))
    print("Random List\n"+str(NUMS))

    # Concave sort
    if config('DO_CONCAVE'):
        concave_nums = sorts.concave(NUMS)
        print_list("Concave Sort", concave_nums)

    # Quick sort
    if config('DO_QUICK'):
        quick_nums = sorts.quick(NUMS)
        print_list("Quick Sort", quick_nums)

    # <Insert other sort here>

""" Prints a list with its comparison and access counters """
def print_list (sort_name, nums_list):
    print(sort_name+"\nComparisons: "+str(nums_list['comparisons'])+"\nAccesses: "+str(nums_list['accesses'])+"\n"+str(nums_list['sorted_list']))
    print("Is it sorted? "+str(helpers.is_sorted(nums_list['sorted_list'])))

if __name__ == '__main__':
    main()