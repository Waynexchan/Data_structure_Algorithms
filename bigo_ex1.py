'''
// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
  let a = 10; //o(1)
  a = 50 + 3; //o(1)

  for (let i = 0; i < input.length; i++) { //o(n)
    anotherFunction(); //o(n)
    let stranger = true; //o(n)
    a++; //o(n)
  }
  return a; o(1)
}
'''

Big O (3+4n) =>o(n)

