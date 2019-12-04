class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        states = set()
        # x, y = sorted([x, y])
        q = [(0, 0)]
        i = 0
        while q: # and i < 50:
            i += 1
            state = q.pop()
            if state in states:
                continue
            # print(state)
            xi, yi = state
            if xi == z or yi == z or xi + yi == z:
                return True
            
            states.add(state)

            # E empty_space in yi -> y - yi
            # amount in xi
            # xi < E -> (0,      yi + xi)
            # xi = E -> (0,      y)
            # xi > E -> (xi - E, yi + xi - E)

            # pour x -> y till y is full
            if xi > 0:
                E = y - yi
                if E == 0:
                    nxi, nyi = xi, yi
                elif xi < E:
                    nxi, nyi = 0, yi + xi
                elif xi == E:
                    nxi, nyi = 0, y
                else:
                    # if less in xi than empty space, pour all
                    nxi, nyi = xi - E, yi + E

                # print(f'(x:{xi} y:{yi}) x->y {E}: ({nxi}, {nyi})')
                q.append((nxi, nyi))

            # pour y -> x
            if yi > 0:
                E = x - xi
                if E == 0:
                    nxi, nyi = xi, yi
                elif yi < E:
                    # if more than empty_space
                    # am = min(xi - empty_y, xi)
                    nxi, nyi = yi + xi, 0
                elif yi == E:
                    nxi, nyi = x, 0
                else:
                    # if less in xi than empty space, pour all
                    nxi, nyi = xi + E, yi - E

                #  print(f'(x:{xi} y:{yi}) y->x {E}: ({nxi}, {nyi})')
                q.append((nxi, nyi))

            # fill x
            q.append((x, yi))
            
            # fill y
            q.append((xi, y))
            
            # dump x

            q.append((0, yi))
            # dump y
            q.append((xi, 0))
            # print(i)
            
        
        return False

def run():
    tests = [
        [3,5,4], [13,11,1], [2,6,5]
    ]
    sol = [
        True, True, False
    ]
    obj = Solution()
    for test, sol in zip(tests,sol):
        print(f'---------------\n{str(test)}\n-----------------')
        res = obj.canMeasureWater(*test)
        print(test, sol, res)
        assert res == sol


if __name__ == '__main__':
    run()