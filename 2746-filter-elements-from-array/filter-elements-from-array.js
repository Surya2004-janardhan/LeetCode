/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {

    const res = []

    arr.forEach((ele, ind) => fn(ele, ind)? res.push(ele) : "EmoTeldhu")
    return res
};