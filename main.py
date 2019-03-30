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
        print("Concave Sort\nComparisons: "+str(concave_nums['comparisons'])+"\nAccesses: "+str(concave_nums['accesses'])+"\n"+str(concave_nums['sorted_list']))
        print("Is it sorted? "+str(helpers.is_sorted(concave_nums['sorted_list'])))

    # Quick sort
    if config('DO_QUICK'):
        pass

    # <Insert other sort here>

if __name__ == '__main__':
    main()