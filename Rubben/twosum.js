function twoSum (nums, target) {
    const num = {}
    for (let i = 0; i < nums.length; i++) {
        let res = target - nums[i]
        if (num.hasOwnProperty(res)) {
            return [num[res], i]
        }
        num[nums[i]] = i
    }
}
console.info(twoSum([1,2,3,4,5,6,7,8,9,10], 5))