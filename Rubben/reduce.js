var reduce = function(nums, fn, init) {
    let res = init
    if (nums === null ) return res

    nums.forEach((item, i) => {
        res = fn(res, nums[i])
    })
    return res

};