import numpy as np
from typing import List
from string import ascii_uppercase
from collections import defaultdict as ddict


class Excel:
    def __init__(self, H: int, W: str):
        r, c = self.parse_rc(H, W)
        self._data = np.zeros((r+1, c+1), dtype=int)

        # pointers to stuff that depends on cell
        self._fwd = ddict(set)      # (r, c) -> [fn(r, c) ... ]
        self._loc2fn = ddict(list)  # target cell fn(r, c) -> [fn(range) ... ]

    @classmethod
    def col2n(cls, col):
        return ascii_uppercase.index(col)

    @classmethod
    def parse_coln(cls, st: str):
        """ A1 -> (0, 0)
            A2 -> (1, 0)
            B26 -> (25, 1)
        """
        return int(st[1:]) - 1, cls.col2n(st[0])

    @classmethod
    def parse_rc(cls, r: int, c: str):
        return r-1, cls.col2n(c[0])

    @classmethod
    def parse_range(cls, st: str) -> tuple:
        """ returns a 4 tuple """
        if ':' in st:
            top, bottom = st.split(':')
            r1, c1 = cls.parse_coln(top)
            r2, c2 = cls.parse_coln(bottom)
            return r1, r2+1, c1, c2+1
        else:
            r1, c1 = cls.parse_coln(st)
            return r1, r1 + 1, c1, c1 + 1

    @classmethod
    def iter_range(cls, fn_range: tuple):
        r1, r2, c1, c2 = fn_range
        for i in range(r1, r2):
            for j in range(c1, c2):
                yield i, j

    def _calc(self, changed: tuple):
        """recalculate all dependecies for a 2-tuple (row, col)"""
        q = [changed]
        while q:
            rc = q.pop()
            if rc not in self._fwd:
                continue

            # recalculate if there is associated funcitons
            for ij in self._fwd[rc]:
                if ij in self._loc2fn:
                    self._data[ij] = 0
                    for r1, r2, c1, c2 in self._loc2fn[ij]:
                        self._data[ij] += np.sum(self._data[r1:r2, c1:c2])

                if ij in self._fwd:
                    q.append(ij)

    def _del_fn(self, rc):
        if rc in self._loc2fn:
            fn_ranges = self._loc2fn.pop(rc)
            # remove fn
            for fn_range in fn_ranges:
                for ij in self.iter_range(fn_range):
                    if rc in self._fwd[ij]:
                        self._fwd[ij].remove(rc)

    def set(self, r: int, c: str, v: int) -> None:
        """
        case 1 set cell -> cell : recalculate
        case 2 set fn -> cell  : del_funcs, recalculate
        """
        rc = self.parse_rc(r, c)
        print(r, c, rc)
        self._data[rc] = v

        if rc in self._loc2fn:
            self._del_fn(rc)

        if rc in self._fwd:
            self._calc(rc)

    def get(self, r: int, c: str) -> int:
        return self._data[self.parse_rc(r, c)]

    def _sum(self, fn_rc):
        return

    def _set_fn(self, rc, strs):
        for s in strs:
            range_tuple = self.parse_range(s)
            for ij in self.iter_range(range_tuple):
                self._fwd[ij].add(rc)

            self._loc2fn[rc].append(range_tuple)

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        """
        case 1 set cell -> fn
        case 2 set fn   -> fn2 :: del_func, set_func, recalculate
        """
        rc = self.parse_rc(r, c)
        self._del_fn(rc)
        self._set_fn(rc, strs)

        # caclulate value
        value = 0
        for r1, r2, c1, c2 in self._loc2fn[rc]:
            value += np.sum(self._data[r1:r2, c1:c2])

        self._data[rc] = value

        # caclulate anyone that depends on r,c
        self._calc(rc)

        return int(value)

    def __repr__(self):
        c = self._data.shape[1]
        s = f'   {"  ".join([ascii_uppercase[i] for i in range(c)])}'
        for r in range(self._data.shape[0]):
            s += f'\n{r+1} {self._data[r].tolist()} '
        return s


def run2():
    tests = [
        [
            ["Excel", "set", "sum", "set"],
            [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2]]
         ]
    ]

    from pprint import pprint

    for test in tests:
        cmds, params = test
        cmds.pop(0)
        params.pop(0)
        obj = Excel(3, 'C')
        for cmd, param in zip(cmds, params):
            v = getattr(obj, cmd)(*param)
            print(obj._loc2fn)
            pprint(obj._fwd)
            print(obj)

    # param_1 = obj.set(1, 'A', 2)

    # param_2 = obj.sum(3, 'C', ['A1', 'A1:B2'])
    # print(obj._loc2fn)
    # pprint(obj._fwd)
    # print(obj)
    # param_3 = obj.set(2, 'B', 2)
    # # param_2 = obj.get(1, 'A')
    # print(obj._loc2fn)
    # pprint(obj._fwd)
    # print(obj)


def run():
    from pprint import pprint
    obj = Excel(6, 'D')
    # ()
    assert obj.parse_range('A1:A1') == (0, 1, 0, 1)
    assert obj.parse_range('A1:B1') == (0, 1, 0, 2)
    assert obj.parse_range('A1:B2') == (0, 2, 0, 2)

    obj.set(1, 'A', 2)
    obj.set(2, 'A', 2)
    param_2 = obj.get(1, 'A')
    param_3 = obj.sum(4, 'B', ['', 'A1:B2'])
    print(obj)
    print(obj._loc2fn)
    pprint(obj._fwd)
    param_4 = obj.sum(3, 'B', ['', 'A1:B2'])
    print(obj)
    print(obj._loc2fn)
    pprint(obj._fwd)
    param_5 = obj.sum(6, 'D', ['', 'A1:B4'])

    print(param_3)
    print(obj)
    print(obj._loc2fn)
    pprint(obj._fwd)
    obj.set(4, 'B', 0)
    obj.set(2, 'B', 3)
    print(obj._loc2fn)
    pprint(obj._fwd)
    print(obj)

if __name__ == '__main__':
    run2()

