def nextGreaterElement(self, nums1, nums2):
        
    nid = {n:i for i,n in enumerate(nums1)}
    res = [-1] * len(nums1)
    stack = []

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            idx = nid[val]
            res[idx] = cur
        if cur in nid:
            stack.append(cur)
                
    return res
