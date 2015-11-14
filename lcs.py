def lengthOfLIS( nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        if len(nums) == 0 or len(nums)==1:

            return len(nums)

        longest = [None]*(len(nums))
        result = float("-inf")
        for i in range(0,len(nums)):
            longest[i]=1
            for j in range(0,i+1):
                if nums[j] < nums[i]:
                    longest[i] = max(longest[i],longest[j]+1)
                result = max(result, longest[i])
        return result
A= [10,9,2,5,3,4]
print lengthOfLIS(A)
