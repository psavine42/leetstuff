from typing import List
import itertools

class Solution:
    strob_map = {'6': '9',
                 '9': '6',
                 '8': '8',
                 '1': '1',
                 '0': '0',
                }

    def isStrobogrammatic(self, num: str) -> bool:
        """https://leetcode.com/problems/strobogrammatic-number"""
        r, l = 0, len(num) - 1

        while r <= l:
            n1 = num[r]
            n2 = num[l]
            if n1 in self.strob_map  and n2 in self.strob_map :
                if n1 != self.strob_map [n2]:
                    return False
            else:
                return False
            r += 1
            l -= 1
        return True

    def findStrobogrammatic(self, n: int) -> List[str]:
        N = n // 2
        res = []
        kys = list(self.strob_map.keys())
        # for


        for combs in itertools.permutations(kys, N):
            # s = []
            if combs[0] == '0' and n != 1:
                continue
            if n % 2 == 0:
                res.append(''.join(list(combs) +
                                   [self.strob_map[num] for num in combs][::-1]))

            else:
                for i in ['0', '1', '8']:
                    res.append(''.join(list(combs) + [i] +
                                       [self.strob_map[num] for num in combs][::-1]))
        return res


class ConfusingNum:
    rmap = {'6': '9',
            '9': '6',
            '8': '8',
            '1': '1',
            '0': '0',
            }

    def confusingNumber(self, N: int) -> bool:
        num = str(N)
        if len(set(num).intersection('23457')) > 0:
            return False
        l = len(num)
        new = []

        for i in range(l):
            if num[i] not in self.rmap:
                return False
            new.append(self.rmap[num[i]])

        return num != ''.join(reversed(new))

    def confusingNumberII(self, N: int) -> int:
        return sum([self.confusingNumber(i) for i in range(N)])


def run():
    tests = [

    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer

def runc():
    c = ConfusingNum()
    for i in [20, 100, 1000, 10000, 100000, 1000000]:
        x = c.confusingNumberII(i+1)
        print(i, x, i/x)

if __name__ == '__main__':
    runc()




