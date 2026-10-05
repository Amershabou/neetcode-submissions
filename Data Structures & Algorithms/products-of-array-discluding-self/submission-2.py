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
        org = [1] + org
        rev = rev + [1]

        for i in range(1,len(nums)+1):
            org[i-1] = org[i-1] * rev[i]
        return org[:len(org)-1]
                



    



       
        

        