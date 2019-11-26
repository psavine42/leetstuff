
class Atom:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return f'{self.name}{self.count}'

    def __mul__(self, other):
        if isinstance(other, int):
            self.count *= other
            return self

    # def __hash__(self):
    def __str__(self):
        if self.count == 1:
            return self.name
        return f'{self.name}{self.count}'

    def __gt__(self, other):
        if isinstance(other, Atom):
            return self.name.__gt__(other.name)

    def __eq__(self, other):
        if isinstance(other, Atom):
            return self.name.__eq__(other.name)

    def __add__(self, other):
        if isinstance(other, Atom):
            self.count += other.count
            return self


def read_tokens(xs):
    token = xs.pop(0)
    if token.isnumeric():
        while xs and xs[0].isnumeric():
            token += xs.pop(0)
        return int(token)
    elif token.isupper():
        while xs and xs[0].islower() and (not xs[0].isnumeric()) and not(xs[0] in '()'):
            token += xs.pop(0)
        return Atom(token, 1)

    elif token == '(':
        L = []
        while xs[0] != ')':
            L.append(read_tokens(xs))
        xs.pop(0)
        return L
    else:
        raise Exception(f'{token}, {token.isnumeric()}, {token.isupper()}')


def mult(atom_or_expr, n):
    if isinstance(atom_or_expr, list):
        return [mult(atom, n) for atom in atom_or_expr]

    elif isinstance(atom_or_expr, Atom):
        atom_or_expr.count *= n
        return atom_or_expr

    else:
        return atom_or_expr


def eval_expr(expr):
    done = []
    while expr:
        curr = expr.pop()
        if isinstance(curr, int):
            atom_or_list = expr.pop()
            if isinstance(atom_or_list, list):
                atom_or_list = eval_expr(atom_or_list)
                atom_or_list = mult(atom_or_list, curr)
                done.extend(atom_or_list)
            else:
                done.append(mult(atom_or_list, curr))

        elif isinstance(curr, list):
            done.extend(eval_expr(curr))

        elif isinstance(curr, Atom):
            done.insert(0, curr)
    # import itertools
    return done


class Solution:
    """ https://leetcode.com/problems/number-of-atoms/
    Runtime: 36 ms, faster than 72.70% of Python3 online submissions for Number of Atoms.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Atoms.

    """
    def countOfAtoms(self, formula: str) -> str:
        fl = list(formula)
        ops = []
        while fl:
            ops.append(read_tokens(fl))

        # eval
        ops = eval_expr(ops)
        ops.sort()

        final = [ops.pop(0)]
        while ops:
            curr = ops.pop(0)
            if final[-1].name == curr.name:
                final[-1] = final[-1] + curr
            else:
                final.append(curr)
        return ''.join([str(x) for x in final])


def run():
    tests = {
        "H2O": "H2O",
        "Mg(OH)2": "H2MgO2",
        "K4(ON(SO3)2)2": "K4N2O14S4"

    }
    s = Solution()
    for t, answer in tests.items():
        print(f'{t}---------------------')
        res = s.countOfAtoms(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()



