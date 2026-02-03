/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    cache = {}
    return function(...args) {
    const key = JSON.stringify(args);

    if (key in cache) {
      return cache[key];
    }

    const result = fn.apply(this, args);
    cache[key] = result;

    return result;
  };
}

const memoizedSum = memoize(function (a, b) {
  return a + b;
});

const memoizedFib = memoize(function (n) {
  if (n <= 1) {
    return 1;
  }

  return memoizedFib(n - 1) + memoizedFib(n - 2);
});

const memoizedFactorial = memoize(function (n) {
  if (n <= 1) {
    return 1;
  }

  return memoizedFactorial(n - 1) * n;
});



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */