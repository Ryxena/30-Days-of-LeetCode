var filter = function(arr, fn) {
    let arraw = []
    arr.forEach((item, i) => {
        if (fn(arr[i], i)) arraw.push(item)
    })
    return arraw
};