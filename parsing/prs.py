
import ast


class VarNode:
    def __init__(self, coef, var=None):
        self.c = coef
        self.var = var

    @classmethod
    def from_str(cls, name):
        # if name
        s = name.replace('x', '').replace('+', '')
        m = -1 if s and s[0] == '-' else 1
        s = s.replace('-', '')
        if s:
            c = m* int(s)
        else:
            c = m* 1
        return VarNode(c)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return VarNode(other.c + self.c)
        return None

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return VarNode(other.c - self.c)
        return None

    def __repr__(self):
        return f'{self.c}x'


class Solution:
    def __call__(self, st):
        return self.solveEquation(st)

    def reduce_expr(self, expr):
        chunks = 0
        nvars = VarNode(0)
        prev = 0
        # print(expr)
        for i in range(len(expr)):
            if expr[i] in '+-=' and prev != i:
                ex = expr[prev:i]
                if 'x' in ex:
                    nvars = nvars + VarNode.from_str(ex)
                else:
                    chunks += int(ex)
                prev = i
        print(nvars, chunks)
        return nvars, chunks

    def solveEquation(self, equation):
        print(equation)
        lh, rh = equation.split('=')
        (lx, lc), (rx, rc)= self.reduce_expr(lh+'='), self.reduce_expr(rh+'=')
        xvar = lx - rx
        coef = lc - rc
        print(xvar, coef)
        if xvar.c == 0 and coef == 0:
            return "Infinite solutions"
        elif xvar.c == 0 and coef != 0:
            return "No solution"
        return f'x={coef // xvar.c}'


def run():
    tests = ["x+5-3+x=6+x-2", "2x=x", "x=x", "2x+3x-6x=x+2" , "-2x=-x+2"]
    s = Solution()
    for x in tests:
        res = s(x)

        print(f'------------\n{res}\n---------')

if __name__ == '__main__':
    run()

