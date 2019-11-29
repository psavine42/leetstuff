class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        width = 0
        current = []

        def pack(current):
            # pack the current
            lens = [len(w) for w in current]
            n = len(lens)
            ttl = sum(lens)
            to_fill = maxWidth - ttl

            # lets say 3 words 7 spaces

        while words:
            w = words.pop(0)
            l = len(w)
            if l + width < maxWidth:
                res.append(pack(current))
                width = 0
                current = []
            else:
                current.append(w)
                width += l + 1

        return res

