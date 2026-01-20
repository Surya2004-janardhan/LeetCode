/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    if (!functions.length) {return function(x) {
        return x
    } }

    return functions.reduceRight(function(prefunc, nextfun) {
        return function(x){
            return nextfun(prefunc(x))
        }
    })
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */