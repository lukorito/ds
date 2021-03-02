// Given an array of integers, write the code to return an array showing the cumulative sum at each index of the original array
// [1,2,3,4,5]
// [1,3,6]

const cumulativeSum = (arr) => {
  const result = [];
  let runningSum = 0;
  for (let i = 0; i < arr.length; i++) {
    runningSum = runningSum + arr[i];
    result.push(runningSum);
  }
  return result;
};

console.log(cumulativeSum([1, 2, 3, 4, 5]));
