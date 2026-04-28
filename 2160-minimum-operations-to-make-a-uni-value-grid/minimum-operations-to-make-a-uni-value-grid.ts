function minOperations(grid: number[][], x: number): number {
    let m = grid.length
    let n = grid[0].length
    let ans = 0
    let res = []
    for (let row of grid){
        for( let ele of row){
            res.push(ele)
        }
    }

res.sort((a, b) => a - b)
    let median = res[Math.floor(res.length / 2)]
 let compare = res[0] % x
  for (let i = 0; i< res.length; i++){
            let rem = res[i] % x
        if (compare !== rem){
            return -1
        }
        ans += Math.abs(res[i] - median) / x
    }
  
    return ans
};