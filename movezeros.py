def moveZeroes(nums):
        n = len(nums)
        i = 0
        last = 0
        while i < n:
            if(nums[i] != 0):
                nums[i],nums[last]=nums[last],nums[i]
                last = last+1
            i = i+1
        print nums

nums = [1,2,0,0,4]
moveZeroes(nums)
