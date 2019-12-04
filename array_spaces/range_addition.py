from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length

        for s,e,inc in updates:
            res[s] += inc
            res[e] += inc

        for i in range(1, length):
            res[i] = res[i] + res[i-1]

        return res


def run():
    tests = [  ]
    s = Solution()
    for t, answer in tests:
        print(f'{t}---------------------')
        res = s.getModifiedArray(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        assert res == answer


if __name__ == '__main__':
    run()




