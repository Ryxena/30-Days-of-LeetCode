function expect(val) {
  return {
    toBe: function(expected) {
      return val === expected ? true : (() => { throw new Error('Not Equal'); })();
    },
    notToBe: function(unexpected) {
      return val !== unexpected ? true : (() => { throw new Error('Equal'); })();
    }
  };
}
