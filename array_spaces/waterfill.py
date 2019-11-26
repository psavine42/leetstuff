class Solution:
    """ https://leetcode.com/problems/number-of-atoms/

    """

    def trap(self, height) -> int:
        N = len(height)
        done = 0
        pis = []
        pointers = []  # (i, j)
        prev_height = None
        deltas = [height[i] - height[i-1] for i in range(1, N)]
        print(deltas)

        for i in range(1, N):
            curr_height = height[i]
            prev_height = height[i - 1]

            if curr_height >= prev_height:
                # height increased
                # check if any pointers get removed
                this_a = curr_height - prev_height
                new = []
                while pointers:
                    si, h, area = pointers.pop()
                    if curr_height >= h:
                        # kill the pointer
                        done += area
                        pis.append([si, i-1, h, area])
                    else:
                        new.append([si, h, this_a + area])
                pointers = new

            elif curr_height < prev_height:
                # move down - add a pointer
                h = prev_height - curr_height

                pointers.append([i-1, h, h])

            # else:

        print(pis)
        return done



def run():
    tests = [
        [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6]
    ]
    s = Solution()
    for t, answer in tests:
        print(f'-----------------\n{t}\n--------------')
        res = s.trap(t)
        print(f'\n{t} --> {res}, {answer}, {res == answer}')
        # assert res == answer


if __name__ == '__main__':
    run()

