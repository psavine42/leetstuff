from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        width = 0
        current = []

        def pack(curr):
            # pack the current stack
            lens = [len(w) for w in curr]
            n = len(lens)
            if n > 1:
                s = ''
                spaces = maxWidth - sum(lens)
                base, add = divmod(spaces, n-1)
                for i in range(n):
                    s += curr[i]
                    if i != n - 1:
                        s = s + ' ' * (base + (i < add))
                return s
            else:
                return pack_last(curr)

        def pack_last(curr):
            s = ' '.join(curr)
            s += ' ' * (maxWidth - len(s))
            return s

        while words:
            w = words.pop(0)
            l = len(w)
            if not words:
                if current and l + width > maxWidth:
                    res.append(pack(current))
                    res.append(pack_last([w]))
                else:
                    res.append(pack_last(current + [w]))
                return res

            elif l + width > maxWidth:
                res.append(pack(current))
                width = 0
                current = []

            current.append(w)
            width += l
            if width < maxWidth:
                width += 1

        return res


def run():
    tests = [
        [
            "This", "is", "an", "example", "of", "text", "justification."
         ],
        [
            "What", "must", "be", "acknowledgment", "shall", "be"
        ],
        [
            "Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
            "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"
        ],
        [
            'longword', 'sevenxx', 'to', 'i', 'a'
        ],
        ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
         "your", "country"],


    ]
    mws = [16, 16, 20, 10, 16]
    targets = [
        [
            "This    is    an",
            "example  of text",
            "justification.  "
        ],
        [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ],
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ],
        ['longword  ',
         'sevenxx to',
         'i a       '
         ],
        ["ask   not   what",
         "your country can",
         "do  for  you ask",
         "what  you can do",
         "for your country"]
    ]

    s = Solution()
    for inp, w, answer in zip(tests, mws, targets):
        print(f'-------------------------------')
        res = s.fullJustify(inp, w)
        for i in range(len(answer)):
            print(f'[{res[i]}]\n[{answer[i]}]')

        assert res == answer


if __name__ == '__main__':
    run()


