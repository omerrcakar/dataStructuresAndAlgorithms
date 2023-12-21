"""
Problem 1: Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

# first solition

def solution1(nums:list[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


result = solution1([1,2,3,4,5,1])
print(result)



# second solition
def solution2(nums:list[int]) -> bool:
    return len(nums) != len(set(nums))


result1 = solution2([1,2,3])
print(result1)



"""
Problem2: Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
# my solution but time: O(n^2)  and space: O(n) 
def singleNumber(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        for num in set(nums):
            if nums.count(num) == 1:
                return num

sonuc = singleNumber([2,2,1])
print(sonuc)
            

# Bit manipulation time : O(n) and space O(1)
# XOR işlemi (bit seviyesinde "exclusive or") iki sayının her bir bitinin karşılaştırılması 
# ve bitlerin farklı olması durumunda sonucun 1, aynı olması durumunda ise sonucun 0 olması prensibine dayanır.
def singleNumberSolution(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result = num ^ result
    return result

sonuc = singleNumberSolution([1,2,3,8,8,3,2,1,9])
print(sonuc)
          


"""
Problem3: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
