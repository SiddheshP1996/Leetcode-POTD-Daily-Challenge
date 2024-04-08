class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        sandwiches.reverse()

        while len(sandwiches) > 0:
            target = sandwiches.pop()
            if count[target] > 0:
                count[target] -= 1
            else:
                sandwiches.append(target)
                break
        return sum(count.values())
