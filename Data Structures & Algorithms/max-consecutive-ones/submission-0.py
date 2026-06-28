class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        counter = 0 

        max_streak = 0

        for i in range(len(nums)):
            if (nums[i] == 1): 
                counter += 1                      

            else: 
                counter =0 
            
            max_streak = max(counter,max_streak)
            



        return max_streak
        