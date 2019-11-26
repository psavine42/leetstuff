
def read_str(xs):
    token = xs.pop(0)
    if token.isnumeric():
        while xs and xs[0].isnumeric():
            token += xs.pop(0)
        num = int(token)
        return num
    elif token.isalpha():
        return token
    elif token == '[':
        l = []
        while xs[0] != ']':
            l.append(read_str(xs))
        xs.pop(0)
        return l


def expand(exprs):
    done = ''
    while exprs:
        token = exprs.pop(0)
        if isinstance(token, int):
            chars = exprs.pop(0)
            str_expr = expand(chars)
            for i in range(token):
                done += str_expr

        elif isinstance(token, str):
            done += token
    return done


class Solution:
    """ https://leetcode.com/problems/decode-string/
    Runtime: 28 ms, faster than 92.77% of Python3 online submissions for Decode String.
    Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Decode String.
    """
    def decodeString(self, s: str) -> str:
        ls = list(s)
        exprs = []
        while ls:
            exprs.append(read_str(ls))

        print(exprs)
        expanded = expand(exprs)
        return expanded


def run():
    tests = {
        "3[a]2[bc]": "aaabcbc",
        "3[a2[c]]": "accaccacc",
        "2[abc]3[cd]ef": "abcabccdcdcdef"
    }
    s = Solution()
    for t, answer in tests.items():
        print(f'{t}---------------------')
        res = s.decodeString(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

