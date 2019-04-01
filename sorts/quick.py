import helpers
from config import config
import math

def _quick_sort (nums, lo, hi):
    if lo < hi:
        part = _partition(nums, lo, hi)
        left = _quick_sort(nums, lo, part['index'] - 1)
        right = _quick_sort(nums, part['index'] + 1, hi)
        return {
            "sorted_list": nums,
            "comparisons": left['comparisons'] + right['comparisons'] + part['comparisons'],
            "accesses": left['accesses'] + right['accesses'] + part['accesses'],
        }
    # Break case
    return {'sorted_list': nums, 'comparisons': 0, 'accesses': 0}

def _partition (nums, lo, hi):
    # Get the pivot
    pivot = get_pivot(nums, lo, hi)
    low = lo
    high = hi
    while True:
        while nums[low] < pivot['value']:
            low+=1
        while nums[high] > pivot['value']:
            high-=1
        if low >= high:
            return {'index': high, 'comparisons': 0, 'accesses': 0}
        helpers.swap(nums, low, high)

def get_pivot (nums, lo, hi):
    p_method = config('QUICK')['pivot_method'].lower()
    if p_method == "median":
        low, mid, high = nums[lo], nums[math.floor((lo + hi) / 2)], nums[hi]
        if low < mid and mid < high:
            return {'value': math.floor((lo + hi) / 2)}
        if mid < low and low < high:
            return {'value': low}
        return {'value': high}
    elif p_method == "first":
        return {'value': nums[lo]}
    elif p_method == "last":
        return {'value': nums[hi]}
    elif p_method == "middle":
        return {'value': nums[math.floor((lo + hi) / 2)]}
    raise Exception('Invalid value for QUICK.pivot_method: {}'.format(p_method))


def quick_sort (nums):
    return _quick_sort(nums, 0, len(nums)-1)