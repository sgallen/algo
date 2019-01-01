#! /usr/bin/python3

class Tree:
    def __init__(self, obj):
        self.key = obj
        self.lhs = None
        self.rhs = None

    def insert(self, obj, left=True):
        side = 'lhs' if left else 'rhs'
        sub_tree = Tree(obj)

        if self.__getattribute__(side) is None:
            self.__setattr__(side, sub_tree)
        else:
            sub_tree.__setattr__(side, self.__getattribute__(side))
            self.__setattr__(side, sub_tree)

def main():
    t = Tree('a')
    t.insert('b')
    t.insert('c')
    t.insert('d', left=False)

if __name__ == '__main__':
    main()