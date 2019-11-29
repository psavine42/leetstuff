class Solution:
    """
    https://leetcode.com/problems/integer-to-english-words/
    """
    def numberToWords(self, num: int) -> str:
        """
        max = 2,147,483,647
        """
        dct = {
            '0': '',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
        }

        postfix10 = {
            '1': 'Ten',
            '2': 'Twenty',
            '3': 'Thirty',
            '4': 'Forty',
            '5': 'Fifty',
            '8': 'Eighty'
        }

        teens = {
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '15': 'Fifteen',
            '18': 'Eighteen',
        }

        def chunk3(chars, post):
            hunds = chars[0]
            tens = chars[1]
            ones = chars[2]
            s = []
            if hunds != '0':
                s += [dct[hunds], 'Hundred']

            if tens == '1':
                teen_num = tens + ones
                s += [teens.get(teen_num, dct[ones] + 'teen')]
                ones = '0'

            elif tens != '0':
                s += [postfix10.get(tens, dct[tens] + 'ty')]

            if ones != '0':
                s.append(dct[ones])

            if s:
                s.append(post)
                return ' '.join([x for x in s if x])
            return ''

        numz = str(num).zfill(12)
        if numz == ''.zfill(12):
            return 'Zero'

        posts = ['Billion', 'Million', 'Thousand', '']
        chunks = [[0, 3], [3, 6], [6, 9], [9, 12]]

        res = []
        for idx, postfix in zip(chunks, posts):
            i, j = idx
            res.append(chunk3(numz[i:j], postfix))

        # print(res)
        return ' '.join([x for x in res if x])



