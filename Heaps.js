// MAX
// - Has 2 children (Binary)
// children is less than parent
//  min is opposite
// no order to left or right
// takes least amount of space possible before going down the tree
// left is always filled first
// parent in heep is given by n -1 / 2
class MaxBinaryHead {
  constructor () {
    this.values = [10, 4, 3]
  }

  insert (val) {
    this.values.push(val)
    let index = this.values.length - 1
    let parentIndex
    while (this.values[index] > this.values[parentIndex]) {
      parentIndex = Math.floor((index - 1) / 2);
      [this.values[index], this.values[parentIndex]] = [this.values[parentIndex], this.values[index]]
      index = parentIndex
    }
  }
  // extractMax() {
  //   let maxVal;
  //   if(this.values.length > 0){
  //     maxVal = this.values.shift();
  //     console.log(maxVal)
  //     console.log(this.values)
  //   }
  // }
}

let maxHeap = new MaxBinaryHead()
// maxHeap.insert(3)
// maxHeap.insert(4)
// maxHeap.insert(10)
maxHeap.insert(20)
// maxHeap.extractMax()

console.log(maxHeap.values)
