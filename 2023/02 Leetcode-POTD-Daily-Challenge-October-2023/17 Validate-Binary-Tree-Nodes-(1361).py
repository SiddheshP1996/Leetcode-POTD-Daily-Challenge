class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Combine all child nodes into a set to identify parent nodes.
        allChildren = set(leftChild + rightChild)
        # Find the root node (the node without a parent).
        roots = set(range(n)) - allChildren
        if len(roots) != 1:
            return False
        root = roots.pop()
        seen = set()
        stack = [root]
        # Use DFS to traverse the tree.
        while stack:
            node = stack.pop()
            children = [leftChild[node], rightChild[node]]
            for child in children:
                if child != -1:
                    if child in seen:
                        # The node has a parent already.
                        return False
                    seen.add(child)
                    stack.append(child)
        # Ensure that all nodes have been visited
        # exactly once, except the root.
        return len(seen) == n - 1
