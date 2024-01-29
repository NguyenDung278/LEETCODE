
function f(a,b) {
  const sum = a+b;
  return sum;
}
console.log(f(3,4)); // 7


var f = function(a,b) {
  const sum = a+b;
  return sum;
}
console.log(f(3,4))


/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function() {
        return "Hello World";
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */