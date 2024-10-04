from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skills = 2 * sum(skill) // len(skill)
        chemistry = 0
        count = Counter(skill)

        for currentSkill, skillCount in count.items():
            if skillCount != count[skills - currentSkill]:
                return -1
            chemistry += skillCount * currentSkill * (skills - currentSkill)
        
        return chemistry // 2
