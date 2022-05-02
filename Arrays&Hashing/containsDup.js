// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


var containsDuplicate = function(nums) {
    for(var i = 0; i < nums.length; i++) {
        for(var j = i + 1; j < nums.length; j++) {
            if (nums[i] == nums[j])
            return true;
        }
        return false;
    }
};

numss = [1,2,3,4]
nums = [1,2,3,1]

console.log(containsDuplicate(nums));
console.log(containsDuplicate(numss));