import math
import random
class Node:
    def __init__(self, v, level):
        self.value = v
        self.next = [None] * level
        self.count = 1
    
    @property
    def level(self):
        return len(self.next)

    def __repr__(self):
        return f'<{self.__class__.__name__[0]}>(v:{self.value}, l:{self.level})'


class Head(Node):
    pass


class Skiplist:
    def __init__(self, n=20000):
        self.maxlevel = int(1 + math.log(n, 2))
        self.head = Head(None, 1)
    
    @property
    def level(self):
        return self.head.level 
        
    def _get_random_level(self):
        i = 1
        while random.random() < 1/4 and i < self.maxlevel:
            i += 1
        return i
            
    def search(self, num: int) -> bool:
        node = self.head
        level = self.level
        for i in reversed(range(level)):
            while node.next[i] and node.next[i].value <= num:
                if node.value == num:
                    return True
                node = node.next[i]

        if node is None:
            return False
        return node.value == num
        
    def add(self, num: int) -> None:
        node = self.head
        update = [None] * self.maxlevel
        level = self.level
        for i in reversed(range(level)):
            while node.next[i] and node.next[i].value <= num:
                node = node.next[i]
                if node.value == num:
                    node.count += 1
                    return 
            update[i] = node

        rl = self._get_random_level()
        new = Node(num, level=rl)
        if level < new.level:
            for i in range(new.level - level ):
                self.head.next.append(None)
                update[level + i] = self.head
        
        for i in range(rl):
            new.next[i] = update[i].next[i]
            update[i].next[i] = new
        
        return

    def erase(self, num: int) -> bool:
        preds = [None] * self.maxlevel
        node = self.head
        to_del = None
        for i in reversed(range(self.level)):

            while node.next[i] and node.next[i].value < num:
                node = node.next[i]
            if node.next[i] is None:
                node = self.head
                continue
            if node.next[i].value == num:
                to_del = node.next[i]
            preds[i] = node
        
        if to_del is None:
            # print('not found')
            return False
            
        elif to_del.count > 1:
            to_del.count -= 1
            return True
        
        nl = to_del.level
        for i in range(nl):
            preds[i].next[i] = to_del.next[i]
        return True
        
    def __repr__(self):
        
        sf = []
        n = 0
        l = []
        curr = self.head
        while curr:
            l.append(curr.value)
            curr = curr.next[0]
            
        for i in range(self.level):
            s = f'{i} : '
            curr = self.head
            j = 0
            while curr:
                v = curr.value
                absj = l.index(v) 
                if absj != j:
                    for k in range(absj - j):
                        s += f'------'
                s += f'-> [{curr.value}]'
                curr = curr.next[i]
                j += 1

            s += '->  nil\n'
            sf.append(s)
        return ''.join(sf[::-1]) 
        

if __name__ == '__main__':
    sl = Skiplist()
    sl.maxlevel = 2
    sl.add(5)
    sl.search(5)
    sl.add(4) 
    sl.add(3)
    sl.add(3) 
    assert sl.search(7) == False

    sl.add(10)
    assert sl.search(3) == True
    assert sl.search(5) == True
    print(sl)
    sl.erase(3)
    sl.erase(5)

    print(sl)


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)