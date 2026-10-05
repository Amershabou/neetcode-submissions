class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        org = [0] * len(nums)
        rev = [0] * len(nums)
        revered = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                org[i] = nums[i]
            else:
                org[i] = nums[i] * org[i-1]

        for i in range(len(nums)):
            if i == 0:
                rev[i] = revered[i]
            else:
                rev[i] = revered[i] * rev[i-1]
        
        rev = rev[::-1]

        res = [0] * len(nums)

        for i in range(len(nums)):
            pre = 1
            suf = 1
            if i > 0:
                pre = org[i -1]
            if i < len(nums) - 1:
                suf = rev[i+1]
            res[i] = pre * suf
        return res
                



        # [48, 24, 12, 8]


    



       
        

        