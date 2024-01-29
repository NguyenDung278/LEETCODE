
const object = {
  "num": 1,
  "str": "Hello World",
  "obj": {
    "x": 5
  }
};

const val = object.obj.x;
console.log(val)

const val1 = object['obj']['x'];
console.log(val1)

const {num,str} = object
console.log(num,str)


class Person {
  constructor(name,age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    console.log("My name is",this.name);
  }
}

const alice = new Person("Alice",25)
alice.greet();

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let currentCount = init;
  return {
  increment: function() {
      currentCount +=1;
      return currentCount;
  },
  decrement: function() {
      currentCount -=1;
      return currentCount;
  },
  reset: function(){
      currentCount = init;
      return currentCount;
  },
  }
};

/**
* const counter = createCounter(5)
* counter.increment(); // 6
* counter.reset(); // 5
* counter.decrement(); // 4
*/


/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let currentCount = init;
  return {increment: () =>++currentCount,
          decrement: () =>--currentCount,
          reset: () => (currentCount= init),
  }
  
};

/**
* const counter = createCounter(5)
* counter.increment(); // 6
* counter.reset(); // 5
* counter.decrement(); // 4
*/