'''
Tuesday, 9/11/18

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def mult_list_not_i(nums):
    mult_nums = [1] * len(nums)
    for j in mult_nums:
        new_j = j
        for i in nums:
            new_j *= i
        new_j /= nums[mult_nums.index(j)]
        mult_nums[mult_nums.index(j)] = new_j
    print(mult_nums)
    return mult_nums


if __name__ == "__main__":
    nums = [1, 2, 3]
    mult_list_not_i(nums)
