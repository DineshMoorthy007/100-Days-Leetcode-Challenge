def containsDuplicate(self, nums):
    return True if len(nums) != len(set(nums)) else False

        #duplicate = set()

        #for num in nums:
        #    if num in duplicate:
        #        return True
        #    duplicate.add(num)
        #return False
