class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        degreeIn = defaultdict(int)
        degreeOut = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            degreeOut[start] += 1
            degreeIn[end] += 1
        
        startNode = pairs[0][0]
        for node in graph:
            if degreeOut[node] > degreeIn[node]:
                startNode = node
                break
        
        stack = [startNode]
        result = []
        
        while stack:
            while graph[stack[-1]]:
                nextNode = graph[stack[-1]].popleft()
                stack.append(nextNode)
            result.append(stack.pop())
        
        result.reverse()
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]
