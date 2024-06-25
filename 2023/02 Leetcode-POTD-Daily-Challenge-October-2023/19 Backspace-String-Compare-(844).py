class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = len(s) - 1
        b = len(t) - 1

        def get_next_char(w, pos, rollback):
            if pos < 0:
                return "", -1
            if w[pos] != '#':
                if rollback > 0:
                    return get_next_char(w, pos - 1, rollback - 1)
                return w[pos], pos - 1
            return get_next_char(w, pos - 1, rollback + 1)

        def get_next_iteractive(w, pos):
            rollback = 0
            while pos >= 0:
                if w[pos] != '#':
                    if rollback > 0:
                        pos -= 1
                        rollback -= 1
                        continue
                    break
                pos -= 1
                rollback += 1
            if pos < 0:
                return "", -1
            return w[pos], pos - 1

        while a >= 0 and b >= 0:
            cs, a = get_next_iteractive(s, a)
            ct, b = get_next_iteractive(t, b)
            if cs != ct:
                return False
        if a < 0 and b < 0:
            return True
        while a >= 0:
            cs, a = get_next_iteractive(s, a)
            if cs != "":
                return False
        while b >= 0:
            ct, b = get_next_iteractive(t, b)
            if ct != "":
                return False
        return True
