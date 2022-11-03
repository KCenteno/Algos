def containsDuplicate(nums):
    # i to make a set
        thiset = set()
        # make a for loop
        for s in nums:
            # check in nums in set
            if s in thiset:
                # if true return True
                return True
            # if not False
            thiset.add(s)
        return False


print(containsDuplicate([1,2,3,4,5,6,7,8,9,10,11,12,13,15,15]))
print(containsDuplicate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))