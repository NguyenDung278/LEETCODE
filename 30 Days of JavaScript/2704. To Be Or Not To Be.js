function createPerson(name,age) {
  return {
    name: name,
    age: age,
    greet: function() {
      console.log(`Hello, my name is ${this.name} and I'm ${this.age} year old.`)
    }
  };
}
let person = createPerson("Alice",25);
person.greet();

let = arr = [5,2,8,1]
let result = arr.sort().reverse().join("-");
console.log(result)


function checkName(name) {
  if (name=== ''){
    throw "Name can't be empty"
  }
  return name;
}
try {
  console.log(checkName(''));
} catch (error) {
  console.error(error)
}

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
  return {
    toBe: (val2) => {
      if(val !== val2) throw new Error("Not Equal");
      return true;
    },
    notToBe: (val2) => {
      if(val === val2) throw new Error("Equal");
      return true;
    }
  };
};
