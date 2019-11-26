class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        states = set()
        x, y = sorted([x, y])
        q = [(0, 0)]
        
        while q:
            state = q.pop()
            if state in states:
                continue
                
            if state[0] == z or state[1] == z or state[0] + state[1] == z:
                return True
            
            states.add(state)
            print(state)
            xi, yi = state
            
            # pour x -> y
            # am = min(y, xi+yi)
            empty_y = y - yi
            if x >= empty_y and :
                am = x - empty_y
            else:
                am = empty_y - x
            q.append( (xi-am, yi + am ) )
            
            # pour y -> x
            empty_x = x - xi
            if y >= empty_x:
                am = y - empty_x
            else:
                am = empty_x - y
            q.append( (xi + am, yi - am)  )
            
            # fill x
            q.append((x, yi))
            
            # fill y
            q.append((xi, y))
            
            # dump x 
            q.append((0, yi))
            # dump y
            q.append((xi, 0))
            
        
        return False

if __name__ == '__main__':
    