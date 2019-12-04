
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'({self.__class__.__name__}: {self.val})'


class CodecBST:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'

        res = []
        n = 1
        q = [(root, 0)]
        while q:
            el, idx = q.pop()
            l, r = el.left, el.right

            # compute index of child
            # add el to res as
            # ch =

            #     ch.append(-l.val)


            if ch:
                n += 1
            #     for n in ch

        s = f"[{','.join([str(x) for x in res])}]"
        print(s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if not data:
            return None

        data = data.split(',')
        if len(data) == 1:
            # root cannot be null ?
            return TreeNode(int(data[0]))

        root = TreeNode(int(data.pop(0)))
        level_size = 1
        prev_level = [root]
        while data:
            nodes = data[0:level_size]
            for i in range(len(nodes)):
                if nodes[i] == 'null':
                    pass

                else:
                    node = TreeNode(int(nodes[i]))
                    parent = prev_level[i//2]
                    if i % 2 == 0:
                        parent.left = node
                    else:
                        parent.right = node


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'

        level = [root]
        res = [root.val]

        while level:
            # if a node has children
            # [c1, c2] if left only [c1, none] if left only [none, c2]
            tmp = []
            n = len(level)
            for i in range(n):
                node = level[i]
                if node:
                    tmp.append(node.left)
                    tmp.append(node.right)

            # print([x.val if x else None for x in tmp])
            if any(tmp):
                level = tmp
                res += [x.val if x else None for x in tmp]
            else:
                level = None

        while res[-1] == None:
            res.pop()

        s = f"[{','.join([str(x) for x in res])}]"
        # print(s)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if not data:
            return None

        data = data.replace(' ', '').split(',')
        if len(data) == 1:
            # root cannot be null ?
            return TreeNode(int(data[0]))

        root = TreeNode(int(data.pop(0)))
        level_size = 2
        prev_level = [root]
        while data:
            level = []
            i = 0
            while i < level_size and data:
                val = data.pop(0)
                if val != 'None':
                    node = TreeNode(int(val))
                    parent = prev_level[i//2]

                    if i % 2 == 0:
                        parent.left = node
                    else:
                        parent.right = node

                    level.append(node)

                i += 1
            if not level:
                break
            prev_level = level
            level_size = len(level) * 2
        return root


def run():
    """
        1
       / \
      2   3
         / \
        4   5

        1
         \
          3
         /
        4

         1
       /  \
      2    3
     /\   / \
    6 7  4   5

         1
       /  \
      2    3
     /\
    6 7

    """
    tests = [
        [1,2,   3,None,None,4,5],
        [1,None,3,4],
        [5, 4, 7, 3, None, 2, None, -1, None, 9],
        [1]
    ]
    s = Codec()
    for t in tests:
        t = str(t).replace(" ", "")
        print(f'-----------------\n{t}\n--------------')
        tree = s.deserialize(t)
        res = s.serialize(tree)
        print(f'\n{t} --> {res}')
        assert t == res


if __name__ == '__main__':
    run()

