class Node {
  constructor (value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

class BinarSearchTree {
  constructor () {
    this.root = null
  }

  find (val) {
    let current = this.root
    if (!current) {
      return false
    } else {
      while (true) {
        if (current.value === val) {
          return true
        } else if (val > current.value) {
          if (!current.right) {
            return false
          } else {
            current = current.right
          }
        } else if (val < current.value) {
          if (!current.left) {
            return false
          } else {
            current = current.left
          }
        } else {
          return false
        }
      }
    }
  }

  insert (val) {
    const newNode = new Node(val)

    if (!this.root) {
      this.root = newNode
      return this
    } else {
      let current = this.root
      while (true) {
        if (val === current.value) {
          return undefined
        }
        if (val > current.value) {
          if (current.right) {
            current = current.right
          } else {
            current.right = newNode
            return this
          }
        } else {
          if (val < current.value) {
            if (current.left) {
              current = current.left
            } else {
              current.left = newNode
              return this
            }
          }
        }
      }
    }
  }

  BFS () {
    const queue = []
    const visited = []
    let node = this.root

    if (!this.root) {
      return visited
    } else {
      queue.push(node)
      while (queue.length) {
        node = queue.shift()
        visited.push(node.value)
        if (node.left) { queue.push(node.left) }
        if (node.right) { queue.push(node.right) }
      }
      return visited
    }
  }

  DFSPreOrder () {
    const data = []
    function helper (node) {
      data.push(node.value)
      if (node.left) helper(node.left)
      if (node.right) helper(node.right)
    }
    helper(this.root)
    return data
  }

  DFSPostOrder () {
    const data = []
    function helper (node) {
      if (node.left) helper(node.left)
      if (node.right) helper(node.right)
      data.push(node.value)
    }
    helper(this.root)
    return data
  }

  DFSInOrder () {
    const data = []
    function helper (node) {
      if (node.left) helper(node.left)
      data.push(node.value)
      if (node.right) helper(node.right)
    }
    helper(this.root)
    return data
  }
}

const tree = new BinarSearchTree()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(20)
tree.insert(3)
tree.insert(8)
console.log(tree.DFSInOrder())
