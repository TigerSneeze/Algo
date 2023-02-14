def two_pass_hash(nums, target):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i
    for j in range(len(nums)):
        diff = target - nums[j]
        if diff in hash and hash[diff] != j:
            return [j, hash[diff]]

def one_pass_hash(nums, target):
    hash = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash:
            return ([i, hash[diff]])
        hash[nums[i]] = i
