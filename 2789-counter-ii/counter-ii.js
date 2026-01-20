/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    temp = init
    return {
    increment : () => ++init,
    reset : () => {
        init = temp
        return  temp},
    decrement : () => --init
    }
 };

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */