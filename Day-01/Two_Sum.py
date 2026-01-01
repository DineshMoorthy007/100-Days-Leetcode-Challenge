def twoSum(self, nums, target):
    num_dict = {}

    for i,num in enumerate(nums):
        compliment = target-num
        if compliment in num_dict :
            return (num_dict[compliment],i)
        num_dict[num] = i 
