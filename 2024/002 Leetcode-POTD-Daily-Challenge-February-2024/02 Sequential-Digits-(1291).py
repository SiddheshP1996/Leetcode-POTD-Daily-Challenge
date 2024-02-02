class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result_array = []
        n = len(str(high))
        current_digit = ['0'] * n

        def execute_digits(i, previous_digit, begin_count):
            if i == n:
                num = int("".join(current_digit))
                if num >= low and num <= high:
                    result_array.append(num)
                return
            if previous_digit == 9:
                return
            if not begin_count:
                execute_digits(i + 1, 0, begin_count)
                for j in range(1, 10):
                    current_digit[i] = str(j)
                    execute_digits(i + 1, j, True)
            else:
                current_digit[i] = str(previous_digit + 1)
                execute_digits(i + 1, previous_digit + 1, begin_count)

        execute_digits(0, -1, False)
        return result_array
