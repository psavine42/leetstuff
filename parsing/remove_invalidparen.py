from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        opened, closed = 0, 0
        invalid_closed = []

        i = 0
        while i < len(s):
            if s[i] == '(':
                opened += 1

            elif s[i] == ')':
                if opened > 0:
                    opened -= 1
                else:
                    closed += 1

            print(f'{i} | {opened}, {closed} ')

            if closed > opened and s[i] == ')':
                invalid_closed.append(i)
            i += 1

        print(opened)
        print(invalid_closed)







def run():
    tests = [
        ["()())()", ["()()()", "(())()"]],
        ["(a)())()", ["(a)()()", "(a())()"]],
        [")(", [""]],
        ['()))((()', ['()()']]

    ]
    s = Solution()
    for t, answer in tests:
        print(f'---------------\n{t}\n---------------------')
        res = s.removeInvalidParentheses(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer

if __name__ == '__main__':
    run()
