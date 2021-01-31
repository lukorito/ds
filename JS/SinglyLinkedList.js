class Node {
  constructor (val) {
    this.val = val
    this.next = null
  }
}

class SinglyLinkedList {
  constructor () {
    this.head = null
  }

  add (val) {
    const newNode = new Node(val)
    if (this.head === null) {
      this.head = newNode
    } else {
      let current = this.head
      while (true) {
        if (current.next) {
          current = current.next
        } else {
          current.next = newNode
          return this.head
        }
      }
    }
  }

  reverse () {
    let current = this.head
    let prev = null
    let next

    while (current) {
      next = current.next
      current.next = prev
      prev = current
      current = next
    }
    return prev
  }
}

const linkedList = new SinglyLinkedList()
linkedList.add(5)
linkedList.add(6)
console.log(linkedList.reverse())
