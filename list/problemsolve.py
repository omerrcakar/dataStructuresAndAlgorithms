"""
Problem: Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

# first solition

def solition1(nums:list[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


result = solition1([1,2,3,4,5,1])
print(result)



# second solition
def solition2(nums:list[int]) -> bool:
    return len(nums) != len(set(nums))


result1 = solition2([1,2,3])
print(result1)