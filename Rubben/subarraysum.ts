function checkSubarraySum(nums: number[], k: number): boolean {
    const remainderDict = new Map<number, number>();
    remainderDict.set(0, -1);
    let cumSum = 0;

    for (let i = 0; i < nums.length; i++) {
        cumSum += nums[i];
        const remainder = cumSum % k;

        if (remainderDict.has(remainder)) {
            if (i - remainderDict.get(remainder)! > 1) {
                return true;
            }
        } else {
            remainderDict.set(remainder, i);
        }
    }

    return false;
}
console.log(checkSubarraySum([2,4,3], 6))