def canJump(nums):
    if len(nums) == 0:
        return False
    elif len(nums) == 1:
        return True
    else:
        max_dist = 0
        for i, num in enumerate(nums):
            if i > max_dist:
                return False
            max_dist = max(max_dist, i + num)
        return True

            
