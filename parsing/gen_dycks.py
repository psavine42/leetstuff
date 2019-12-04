


def next_dn(w):
    """ i n te g e r next dyck
    i n t e g e r const a
    i n t e g e r const b
    integer
    c
    c
    c
    return c ;
    }
    ✝
    1
    w o r d ( i n t e g e r w) {
    = w & −w ;
    = w + a;
    = w ˆ b;
    = ( c / a >> 2 ) + 1 ;
    = ( ( c ∗ c − 1) & 0 xaaaaaaaaaaaaaaaa ) | b ;"""
    a = w & -w
    b = w + a
    c = w ^ b
    c = (c // a >> 2) + 1
    c = ((c * c - 1) & 0) | b
    return c

from collections import defaultdict as ddict
from itertools import product


def parens(n):
    cache = ddict(list)
    # for i in range(n):
    #     f'({})' for i in range()

    def solve(num):
        if num not in cache:
            cache[num] = [f'({t[0]}){t[1]}' for i in range(1, num + 1)
                          for t in product(solve(i - 1), solve(num - i))]
        return cache[num]

    return solve(n)


