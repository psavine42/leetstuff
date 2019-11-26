class Solution:



    def __call__(self, *args, **kwargs):
        return


def run():
    tests = [

    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

