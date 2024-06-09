function climbStairs(n: number): number {
    let arr: number[] = [1,2]
    for (let i = 2; i < n; i++) {
        arr[i] = arr[i - 1]+arr[i - 2]
    }
    return arr[n-1]
};