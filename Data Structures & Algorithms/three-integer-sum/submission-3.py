class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        newList = nums.sort()

        res =[]


        #[-4-1,-1,0,1,2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]
                if curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l -1] == nums[l]:
                        l += 1
        return res

            
        



        