class Solution:
    def twoSum(self, nums, target):
        solutions = {target - num : i for i,num in enumerate(nums)}

        for i,num in enumerate(nums):
            if solutions.get(num) != None:
                ans = [i, solutions[num]]
                if ans[0] != ans[1]: return ans