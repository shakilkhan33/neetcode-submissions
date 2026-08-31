class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I need O(n) time solution if possible 
        #step : 1 need to create a set so that I don't get any duplicate values 
        numSet = set(nums)
        l = 0 # hold the longest value 
        for num in numSet: # loop through the nums to check 
            # I need to check previous sequences and has not to be in the sets
            if (num - 1) not in numSet:
                #let say the number is (1-1)= 0 not in set
                length = 1 
                while (num + length) in numSet:
                    # let say num is 0 and + length is 1 = 1
                    # I need to add length since I need find longest length
                    length += 1 # it helps me to count the length 
                l = max(length , l) # I keep the higest length 

        return l # the whole approch gives me O(n) time complexity and it is the most efficient so far.





        
        
        
        