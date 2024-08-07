class Solution:
    def numberToWords(self, num: int) -> str:
        lessThanTwenty = ["", "One", "Two", "Three", "Four", "Five",
                          "Six", "Seven", "Eight", "Nine", "Ten",
                          "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                          "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        tenthPlace = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                      "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        def twoDigit(num):
            if num < 20:
                return lessThanTwenty[num]
            else:
                tens = num // 10
                ones = num % 10
                return tenthPlace[tens] + ("" if ones == 0 else " " + lessThanTwenty[ones])

        def threeDigit(num):
            if not num: return ""
            if not num // 100: return twoDigit(num)
            return lessThanTwenty[num // 100] + " " + \
                'Hundred' + (" " + twoDigit(num % 100) if num % 100 else "")

        billion = num // 1000000000
        million = (num // 1000000) % 1000
        thousand = (num // 1000) % 1000
        hundred = num % 1000

        result = ""
        if billion:
            result += threeDigit(billion) + " Billion"
        
        if million:
            if result: result += " "
            result += threeDigit(million) + " Million"
        
        if thousand:
            if result: result += " "
            result += threeDigit(thousand) + " Thousand"
        
        if hundred:
            if result: result += " "
            result += threeDigit(hundred)

        return result.strip()
