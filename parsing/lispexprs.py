import operator as op


class Lisp:
    def __eq__(self, other):
        # if isinstance(other, Lisp):
        return False

    def __call__(self, ctx=None):
        pass

    # def _eval(self, val, ctx=None):
    #     if isinstance(val, Lisp):
    #         return val(ctx=ctx)
    #     elif isinstance(val, str):
    #         if val in self.vars:
    #             self.vars[sym] = self.vars[val]
    #         elif val in cx:
    #             self.vars[sym] = cx[val]
    #     else:
    #         return val


class Context(Lisp):
    def __init__(self, args):
        self.vars = {}
        self.tokens = args

        assert len(args) % 2 == 1
        self.res = args[-1]
        self._set = 0

    def _setup(self, ctx=None):
        if self._set == 0:
            # self._setup()

            i = 0
            cx = {**ctx, **self.vars} if ctx else self.vars
            while i + 1 < len(self.tokens):
                sym = self.tokens[i]
                val = self.tokens[i+1]
                if isinstance(val, Lisp):
                    self.vars[sym] = val(ctx=cx)
                elif isinstance(val, str):
                    if val in self.vars:
                        self.vars[sym] = self.vars[val]
                    elif val in cx:
                        self.vars[sym] = cx[val]
                else:
                    self.vars[sym] = val
                i += 2

            self._set = 1

    def __repr__(self):
        s = ''
        for k, v in self.vars.items():
            s += f'{k}={v} '
        return f'(LET {s}) -> {self.res}'

    def __getitem__(self, item):
        self._setup()

        if item in self.vars:
            var = self.vars[item]
            if isinstance(var, Expr):
                return var(ctx=self.vars)
            else:
                return var
        return None

    def __call__(self, ctx=None):
        self._setup(ctx=ctx)

        cx = {**ctx, **self.vars} if ctx else self.vars
        if isinstance(self.res, Lisp):
            return self.res(ctx=cx)

        elif isinstance(self.res, int):
            return self.res

        elif isinstance(self.res, str):
            if isinstance(self.vars[self.res], Lisp):
                return self.vars[self.res](ctx=cx)
            else:
                return self.vars[self.res]


class Expr(Lisp):
    def __init__(self, fn, tokens):
        self.tokens = tokens
        self.fn = fn

    def __call__(self, ctx=None):
        nums = []
        for arg in self.tokens:
            if isinstance(arg, str) and ctx is not None:
                val = ctx[arg]
                nums.append(val)
            elif isinstance(arg, Lisp):
                nums.append(arg(ctx=ctx))
            else:
                nums.append(arg)
        return self.fn(nums[0], nums[1])

    def __repr__(self):
        return f'({self.fn.__name__} {",".join([repr(x) for x in self.tokens])})'


opers = {'mult': lambda xs: Expr(op.mul, xs),
         'add': lambda xs: Expr(op.add, xs),
         'let': Context,
         }


def evall(expr, ctx):
    if isinstance(expr, int):
        return expr
    #elif isinstance(expr, Context):
    #    ctx[]

    # else:
    #    fn = eval()


def read_tokens(tokens):
    t = tokens.pop(0)
    if t == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_tokens(tokens))
        tokens.pop(0)
        if L[0] in opers:
            expr_inst = opers[L[0]](L[1:])
            return expr_inst
        else:
            raise Exception()
    else:
        if t.isnumeric() or t[0] == '-':
            return int(t)
        return t


class Solution:
    """ https://leetcode.com/problems/parse-lisp-expression/

    Runtime: 32 ms, faster than 98.39% of Python3 online submissions for Parse Lisp Expression.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Parse Lisp Expression.
    """
    def evaluate(self, expr: str)-> int:
        tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split(' ')
        # build contexts
        tokens = [x for x in tokens if x]
        # read:
        expr = read_tokens(tokens)
        # eval
        return expr()


def run():
    tests = {
        "(let x -2 y x y)": -2,

        '(mult 3 (add 2 3))':15,
        '(let x 2 5)': 5,
        '(mult 3 (add -2 3))': 3,
        '(let x 2 (mult x 5))':10,
        '(let x 3 x 2 x)':2,
        '(let a1 3 b2 (add a1 1) b2)':4,
        '(let x 2 (mult x (let x 3 y 4 (add x y))))':14,

        '(let x 2 (add (let x 3 (let x 4 x)) x))':6,
        '(let x 1 y 2 x (add x y) (add x y))':5,

        '(let x 1 y 2 x (let x 2 x) (add x y))': 4,
        '(add 1 2)': 3,
        '(let x 1 y (let b 3 (add x b)) (add x y))': 5,


    }
    s = Solution()
    for t, answer in tests.items():
        # print('---------------------')
        # print(t)
        print(f'{t}---------------------')
        res = s.evaluate(t)

        print(t, ' --> ', res, answer, res == answer)
        assert res == answer


if __name__ == '__main__':
    run()
