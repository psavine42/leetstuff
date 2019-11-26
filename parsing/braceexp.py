from string import ascii_lowercase
from itertools import product

"""
        while i < l:
            print(i, expression[i], curr)
            if expression[i] in chars:
                atom = expression[i]
                i += 1
                while expression[i] in chars:
                    atom += expression[i]
                    i += 1
                new = SetExpr(atom)
                curr.right = new 
                # stack.append(new)
                
            elif expression[i] == ',':
                # curr.value.append()
                expr = SetExpr(self._union, parent=curr)
                curr.right = expr
                curr = expr
                i += 1

            elif expression[i] == '}':
                # curr = stack.pop()
                curr = curr.parent 
                # if curr is None:

                i += 1
                
            elif expression[i] == '{':
                expr = SetExpr('{', parent=curr)
                curr.right = expr
                # curr = expr
                i += 1
            else:
                raise Exception()
                # while expression
"""
class Atom:
    def __init__(self, value):
        self.v = value

class SetExpr:
    def __init__(self, v=None, r=None, l=None, parent=None):
        self.value = v
        self.right = r
        self.left = l
        self.parent = parent

    def __repr__(self):
        def rbal(v):
            if callable(v):
                return v.__name__
            else:
                return str(v)
        s = f'{rbal(self.value)} ({rbal(self.left)} {rbal(self.right)})'
        # s += self.left.__repr__() if self.left else ''
        # s += self.right.__repr__() if self.right else ''
        return s

class SetExpr2:
    def __init__(self, v=None, r=None, l=None, parent=None):
        self.value = v if v else []
        self.right = r
        self.left = l
        self.parent = parent

    def append(self, v):
        self.value.append(v)

    def __repr__(self):
        g = ', '.join([repr(x) for x in self.value ])
        s = f'[{g}]'
        return s

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.value == self.value 

    def eval(self):
        s = set()
        vals = self.value
        op = None
        # print('------')
        print(vals)

        while vals:
            el = vals.pop()
            print(el, s)
            #if isinstance(el, SetExpr2) and op in [None, ',']:
            #    for x in el.value:
            #        s.add(x)
            if el in ascii_lowercase and op in [None, ',']:
                s.add(el)
                op = None
            elif el == ',':
                op == el
            else:
                s = set(product(s, el))
            
        
        print(self.value, '->', s)
        print('------')
        self.value = s
def evaluatex(exprs):
    done = []
    while exprs:
        expr = exprs.pop(0)

        if isinstance(expr, list):
            expr = evaluate(expr)
        elif expr in ascii_lowercase:
            expr = [expr]

        if len(exprs) == 0:
            done.extend(expr)
            break

        next_op = exprs.pop(0)
        if next_op == ',':
            done.extend(expr)

        if next_op == '*':

            next_val = exprs.pop(0)
            next_expr = evaluate(next_val) if isinstance(next_val, list) else [next_val]
            done.extend(prod(expr, next_expr))
            # next_expr = expr if isinstance(expr, list) else [next_val]
    return done

def ___evaluate2(exprs):
    done = []
    while exprs:
        lh = exprs.pop(0)

        if len(exprs) == 0:
            done.extend(evaluate(lh))
            break

        next_op = exprs.pop(0)
        rh = exprs.pop(0)
        if isinstance(lh, list):
            lh = evaluate(lh)

        if isinstance(rh, list):
            rh = evaluate(rh)

        if next_op == ',':
            done.extend(lh)
            done.extend(rh)

        if next_op == '*':
            done.extend(prod(lh, rh))
            # next_expr = expr if isinstance(expr, list) else [next_val]
    return done


def prod(a, b):
    a = [a] if isinstance(a, str) else a
    b = [b] if isinstance(b, str) else b
    res = []
    for i in a:
        for j in b:
            res.append(i+j)

    return list(set(res))


def union(a, b):
    a = [a] if isinstance(a, str) else a
    b = [b] if isinstance(b, str) else b
    return list(set(a + b))


def evaluate(exprs):
    done = []
    c = [x for x in exprs]

    while exprs:
        if done:
            lh = done # .pop()
        else:
            lh = exprs.pop(0)
            # print(lh)
            if len(exprs) == 0:
                done.extend(evaluate(lh))
                continue

        next_op = exprs.pop(0)
        rh = exprs.pop(0)
        # print('op', lh, next_op, rh)
        if isinstance(rh, list):
            rh = evaluate(rh)

        # print('-----------')
        # print(done)
        # print(exprs)
    print('------')
    print(c)
    print(done)
    return done


class Solution:
    def parse(self, strs):
        token = strs.pop(0)
        if token == '{':
            l = []
            while strs[0] != '}':
                l.append(self.parse(strs))
            strs.pop(0)
            return l  # [x for x in l if x != ',']
        elif token in ascii_lowercase:
            curr = token
            while strs and strs[0] in ascii_lowercase:
                curr += strs.pop()
            return curr
        elif token in '*,':
            return token

    def __braceExpansionII(self, expression):
        tks = expression \
            .replace('{', '*{').replace(',*{', ',{').replace('{*{', '{{')\
            .replace('}', '}*').replace('}*,', '},').replace('}*}', '}}').replace('**', '*') \
            .replace(',', ' , ').replace('{', ' { ').replace('}', ' } ').replace('*', ' * ')
        tks = [x for x in tks.split(' ') if x]
        if tks[0] == '*':
            tks.pop(0)
        if tks[-1] == '*':
            tks.pop()
        # print(tks)
        ops = []
        while tks:
            ops.append(self.parse(tks))

        print(ops)
        print('----')
        # ds = evaluate(ops)
        ds = self.eval(ops)
        # q = [ops.pop(0)]
        print('----')
        print(ds)
        return sorted(list(set(ds)))

    def eval(self, ops):
        res = set()
        stack = []
        while ops:
            op1 = ops.pop(0)
            print(op1)
            if isinstance(op1, list) and not ops:
                ops = op1
                continue

            if isinstance(op1, list):
                pass
            # op2 = ops.pop(0)
            # op3 = ops.pop(0)

            if next_op == '*':
                res = prod(res, rh)

            if next_op == ',':
                res = union(res, rh)

        return res

    def braceExpansionII(self, expression):
        res = []
        stack = []
        level = 0
        i = 0
        N = len(expression)
        curr = []
        while i < N:
            tk = expression[i]
            if tk == '{':
                level += 1
                stack.append(curr[:])
                curr = []
                # while

            elif tk == ',':
                curr.append(expression[i+1])
                i += 1

            else:
                pass
            i += 1

        return sorted(list(set(res)))




def run():
    tests = {
        # "{a,b}{c,d}": {"ac", "ad", "bc", "bd"},
        "{a,b}{c,{d,e}}": {"ac", "ad", "ae", "bc", "bd", "be"},
        "{{a,z},a{b,c},{ab,z}}": {"a", "ab", "ac", "z"},
        # "{{a,b},{b,c}}": ["a","b", "c"],
        # "{a,b},l{c,{d,e}}": ['a', 'b', 'lc', 'ld', 'le'],
        # "{a,b,c}":{"a", "b", "c"},
        # "a{b,c}{d,e}f{g,h}": ["abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"]
    }
    s = Solution()
    for t, answer in tests.items():
        print(f'---------------------\n{t}\n---------------')
        res = s.braceExpansionII(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()



