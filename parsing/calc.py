import operator
from collections import deque


class Solution:
    ops = {
        '+':operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }
    press = [['/', '*'], ['-', '+']]

    def read_str(self, xs):
        token = xs.pop(0)
        if token == '(':
            L = deque()
            while xs and xs[0] != ')':
                L.append(self.read_str(xs))
            xs.pop(0)

            return self.eval_ops(L)

        elif token.isnumeric():
            num = token
            while xs and xs[0].isnumeric():
                num += xs.pop(0)
            return int(num)

        elif token in self.ops:
            return token

    def eval_ops(self, expr_q):

        while len(expr_q) > 1:
            n1 = expr_q.popleft()
            op = expr_q.popleft()
            n2 = expr_q.popleft()
            res = self.ops[op](n1, n2)
            expr_q.appendleft(res)
        return expr_q.pop()

    def calculate(self, s: str) -> int:
        for op in list(self.ops) + ['(', ')']:
            s = s.replace(f'{op}', f' {op} ')
        # print()
        arr = [x for x in s.split(' ') if x]
        # print(arr)
        ops = deque()
        while arr:
            ops.append(self.read_str(arr))

        # print(ops)
        return self.eval_ops(ops)

def run():
    tests = {
        # " 6-4 / 2 ": 4,
        " 2-1 + 2 " : 3,
        "(1+(4+5+2)-3)+(6+8)":23
    }
    s = Solution()
    for t, answer in tests.items():
        print(f'{t}---------------------')
        res = s.calculate(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

