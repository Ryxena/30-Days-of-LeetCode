var sortedSquares = function(nums) {
    return nums.map((x) => Math.pow(x, 2)).sort((a,b) => a - b)
};