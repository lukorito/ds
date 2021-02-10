// You are given an integer N, followed by N lines of input (1 <= N <= 100). Each line of input contains one number M.

// Write a program that goes through the numbers from 1 to M (1 <= M <= 100) and prints out the following:

// For numbers which are multiples of three print "Ona".
// For numbers which are the multiples of five print "Data".
// For numbers which are multiples of both three and five print "OnaData".
// If the conditions above fail for all numbers, print "N/A".
// Example

// input
// 4
// 1
// 4
// 10
// 15
// output
// N/A
// Ona
// Ona Data Ona Ona Data
// Ona Data Ona Ona Data Ona OnaData
const input = "4\n1\n4\n10\n15\n";

const onaData = (input) => {
  let inputArr = input.split("\n");
  let string = "";
  for (let i = 1; i <= parseInt(inputArr[0], 10); i++) {
    let curr = parseInt(inputArr[i], 10);
    let indString = "";
    for (let i = 1; i <= curr; i++) {
      if (i % 5 === 0 && i % 3 === 0) {
        indString += "OnaData ";
      } else if (i % 3 === 0) {
        indString += "Ona ";
      } else if (i % 5 === 0) {
        indString += "Data ";
      }
    }
    if (!indString) {
      indString += "N/A";
    }

    string += indString + "\n";
  }
  console.log(string);
};

onaData(input);
