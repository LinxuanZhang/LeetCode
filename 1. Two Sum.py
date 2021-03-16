def twoSum(nums, target):
    res_dict = {}
    for i in range(len(nums)):
        current, other = nums[i], target - nums[i]
        if str(other) in res_dict:
             return [i, res_dict[str(other)]]
        else:
            res_dict[str(current)] = i



         
