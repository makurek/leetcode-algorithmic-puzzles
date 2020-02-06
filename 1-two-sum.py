'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in nums:
            search = target - i
            try:
                search_index = nums.index(search, nums.index(i)+1, len(nums))
                result.append(search_index)
                result.append(nums.index(i))
                break
            except:
                continue
        return result
'''


# naive solution
def twoSum1(nums, target):
    result = []
    for i in nums:
        search = target - i
        try:
            search_index = nums.index(search, nums.index(i) + 1, len(nums))
            result.append(search_index)
            result.append(nums.index(i))
            break
        except:
            continue
    return result

# optimized solution 1 - single pass hashing table
def twoSum2(nums, target):
    result = []
    d = {}
    # fist pass, let's create a cache
    for index, element in enumerate(nums):
        d[element] = index
    # second pass
    for element in nums:
        search = target - element
        try:
            l = d[search]
            # if the element we are looking for is the current one processed
            if l == nums.index(element):
                continue
            result.append(nums.index(element))
            result.append(l)
            return result
        except KeyError:
            continue


print(twoSum2([3,2,4], 6))
