# Solution 1

"""
Time complexity: O(1)
Space complexity: O(n)
"""

class ListNode:
    def __init__(self, count: int = -1):
        self.prev = None
        self.next = None
        self.words = set()
        self.count = count

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeWord(self, node: ListNode, word: str) -> None:
        node.words.remove(word)

        if not node.words:
            self.removeNode(node)

    def removeNode(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addRightNode(self, currentNode: ListNode, newNode: ListNode) -> None:
        newNode.next = currentNode.next
        currentNode.next.prev = newNode
        newNode.prev = currentNode
        currentNode.next = newNode

class AllOne:
    def __init__(self):
        self.wordToNode = {}
        self.doubleLinkedList = DoubleLinkedList()

    def inc(self, key: str) -> None:
        if key in self.wordToNode:
            currentNode = self.wordToNode[key]
            nextNode = currentNode.next
            count = currentNode.count + 1

            if nextNode.count != count:
                nextNode = ListNode(count)
                self.doubleLinkedList.addRightNode(currentNode, nextNode)

            nextNode.words.add(key)
            self.wordToNode[key] = nextNode
            self.doubleLinkedList.removeWord(currentNode, key)
        else:
            head = self.doubleLinkedList.head
            nextNode = head.next

            if nextNode.count != 1:
                nextNode = ListNode(1)
                self.doubleLinkedList.addRightNode(head, nextNode)
 
            nextNode.words.add(key)
            self.wordToNode[key] = nextNode          

    def dec(self, key: str) -> None:
        currentNode = self.wordToNode[key]
        count = currentNode.count - 1

        if count == 0:
            del self.wordToNode[key]
        else:
            previousNode = currentNode.prev
            nextNode = previousNode

            if previousNode.count != count:
                nextNode = ListNode(count)
                self.doubleLinkedList.addRightNode(previousNode, nextNode)

            nextNode.words.add(key)
            self.wordToNode[key] = nextNode

        self.doubleLinkedList.removeWord(currentNode, key)

    def getMaxKey(self) -> str:
        words = self.doubleLinkedList.tail.prev.words

        if words:
            word = words.pop()
            words.add(word)
            return word
            
        return ""

    def getMinKey(self) -> str:
        words = self.doubleLinkedList.head.next.words

        if words:
            word = words.pop()
            words.add(word)
            return word

        return ""


"""
# Solution 2

'''
Time Complexity: O(1)
'''

class AllOne:

    def __init__(self):
        self.myOneDict = {}

    def inc(self, key: str) -> None:
        if key in self.myOneDict:
            self.myOneDict[key] += 1
        else:
            self.myOneDict[key] = 1

    def dec(self, key: str) -> None:
        if key in self.myOneDict:
            if self.myOneDict[key] > 1:
                self.myOneDict[key] -= 1
            else:
                self.myOneDict.pop(key)

    def getMaxKey(self) -> str:
        if not self.myOneDict:
            return ""
        maxValue = max(self.myOneDict.values())
        
        for key in self.myOneDict.keys():
            if self.myOneDict[key] == maxValue:
                return key

    def getMinKey(self) -> str:
        if not self.myOneDict:
            return ""
        minValue = min(self.myOneDict.values())
        
        for key in self.myOneDict.keys():
            if self.myOneDict[key] == minValue:
                return key
"""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()