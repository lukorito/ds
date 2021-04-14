function binarySearch(arr, target) {
  function search(start, stop, arr, target) {
    if (start > stop) {
      return false;
    }
    let mid = Math.floor((stop + start) / 2);
    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] > target) {
      return search(start, mid - 1, arr, target);
    } else {
      return search(mid + 1, stop, arr, target);
    }
  }
  return search(0, arr.length - 1, arr, target);
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 0));
