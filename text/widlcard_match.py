class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lp = len(p)
        i, j, l = 0, 0, len(s)
        while i < l:
            pj = p[j]
            si = s[i]
            if pj == '*':
                nxtj = pj
                nj = j
                while nxtj not in '*?' and nj < lp:
                    nj += 1
                    nxtj = p[nj]



            elif pj == '?':
                


            elif pj != si:
                return False

            i += 1
        return True

def run():
    tests = [
        "aa"
    ]
    s = Solution()
    for t in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.isMatch(t)
        print(f'\n{t} --> {res}, ')
        # assert res == answer


if __name__ == '__main__':
    run()




