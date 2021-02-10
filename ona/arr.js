// Problem Description
// An array of integers a is called smooth if the absolute value of the difference between any two adjacent elements is less than or equal to 1. You are given an array a. Check whether it is smooth and output "YES" if it is, or "NO" if it is not (quotes for clarity only).

// The first line of the input contains an integer N - the number of elements in the array. 1 <= N <= 10.
// The second line of the input contains N integers - the elements of the array, separated with single spaces. 1 <= ai <= 10.

// Example

// input

// 5
// 3 4 4 5 4

// output

// YES

// input

// 4
// 1 1 8 2

// output

// NO

    let numArr = input.split(" ");
    const arrLength = parseInt(length, 10);
    let i = 0;
    let j = 1;
    if (arrLength === 1) {
      console.log("YES");
      return;
    }
    while (
      i <= 10 &&
      j <= 10 &&
      i < arrLength &&
      j < arrLength &&
      arrLength <= 10
    ) {
      const slowIndex = parseInt(numArr[i], 10);
      const fastIndex = parseInt(numArr[j], 10);
      if (Math.abs(slowIndex - fastIndex) > 1) {
        console.log("NO");
        return;
      }
      if (i === slowIndex || j === fastIndex - 1) {
        console.log("YES");
        return;
      }
      i = i + 1;
      j = j + 1;
    }
};

arraySmooth(input, length);
