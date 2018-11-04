class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for one_tuple in d:
            while num >= one_tuple[0]:
                result += one_tuple[1]
                num -= one_tuple[0]
        return result
