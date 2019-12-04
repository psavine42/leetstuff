class Solution:
    def _lengthOfLongestSubstring(self, s: str) -> int:

        N = len(s)
        if N == 1:
            return 1

        i2chr = {}
        chr2i = {}

        curr = 0
        longest = 0
        for i in range(N):
            ch = s[i]

            if ch in chr2i:

                longest = max(i - chr2i[ch], longest)
                sq = i - chr2i[ch]
                print(ch, sq, longest, chr2i, i2chr)
                for j in range(chr2i[ch] + 1):
                    chr2i.pop(i2chr[j])

            i2chr[i] = ch
            chr2i[ch] = i

        seq = list(reversed(sorted(chr2i.values())))
        curr = 1
        for i in range(1, len(seq)):
            if seq[i - 1] - 1 == seq[i]:
                curr += 1
            else:
                break

        print(longest, chr2i, curr)
        longest = max(longest, curr)
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:

        N = len(s)
        l, r = 0, 1
        longest = 0
        while r < N:
            longest = max(longest, r - l)
            while s[r] in s[l:r]:
                l += 1
            r+=1

        return max(longest, len(s[l:r]))




def run():
    tests = [
        ["aab", 2],
        ["abcabcbb", 3],
        ["bb", 1],
        ["pwwkew", 3],
        [" a", 2],
        [" ", 1],
        ['abdfgdsfag', 5]
    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.lengthOfLongestSubstring(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()

