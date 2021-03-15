// # accepts unsigned values from 0 - 2^20 - 1

// # "13 DUP 4 POP 5 DUP + DUP + -"

const wordMachine = (word) => {
  const wordArr = word.split(" ");
  const stack = [];
  const toNum = (val) => parseInt(val, 10);

  for (let i = 0; i < wordArr.length; i++) {
    let currentItem = wordArr[i];
    let parsedValue = toNum(currentItem);

    if (!isNaN(parsedValue)) {
      stack.push(parsedValue);
    } else if (currentItem === "POP") {
      stack.pop();
    } else if (currentItem === "DUP") {
      if (stack.length === 0) {
        return -1;
      }
      let lastItem = stack[stack.length - 1];
      stack.push(lastItem);
    } else if (currentItem === "+") {
      if (stack.length < 2) {
        return -1;
      }

      let lastItem = stack.pop();
      let secondLastItem = stack.pop();
      const sum = lastItem + secondLastItem;
      if (sum > (2 ^ 20) - 1) {
        return -1;
      }
      stack.push(sum);
    } else if (currentItem === "-") {
      if (stack.length < 2) {
        return -1;
      }
      let lastItem = stack.pop();
      let secondLastItem = stack.pop();
      let difference = lastItem - secondLastItem;
      if (difference < 0) {
        return -1;
      }
      stack.push(difference);
    }
  }
  return stack.pop();
};

// console.log(wordMachine("13 DUP 4 POP 5 DUP + DUP + -"));
// console.log(wordMachine("5 6 + -"));
console.log(wordMachine("3 DUP 5 - -"));
