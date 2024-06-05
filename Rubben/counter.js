var createCounter = function(init) {
  let count = init;

  return {
    increment: () => ++count,
    reset: () => count = init,
    decrement: () => --count
  };
};
