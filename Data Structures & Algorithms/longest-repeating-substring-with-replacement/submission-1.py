class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        # for loop to iterate through the array
        # array that stores left and right of the window
        # lets convert the array to set and see if its length is > k + 1
        
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)
            maxf = max(maxf, count.get(s[r]))
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            
        return res