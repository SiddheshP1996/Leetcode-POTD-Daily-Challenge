from collections import OrderedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        count = OrderedDict()
        hand.sort()
        for h in hand:
            if h in count:
                count[h] += 1
            else:
                count[h] = 1
                
        while len(count) > 0:
            group = []
            items = list(count.items())
            if len(items) < groupSize:
                return False
            
            for cardValue, countOfCard in items:
                if len(group) == 0:
                    group.append(cardValue)
                else:
                    if cardValue != (group[-1] + 1):
                        return False
                    group.append(cardValue)
                count[cardValue] -= 1
                if count[cardValue] == 0:
                    count.pop(cardValue)
                if len(group) == groupSize:
                    break
        return True
