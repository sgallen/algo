#! /usr/bin/python3

from tree import Tree


class ParseTree:
    def __init__(self):
        self.reset()

    def build(self, input):
        self.validate(input)
        input = input.replace(' ', '')  # Remove whitespace

        if self.root is not None:
            raise RuntimeError('Must reset in order to re-build.')

        self.root = Tree('')
        current_tree = self.root

        for item in input:
            if item == '(':
                # Add node to left
                current_tree.insert('')
                self.stack.append(current_tree)
                # Descend to left
                current_tree = current_tree.lhs
            elif item == ')':
                # Ascend to parent
                if self.stack:
                    current_tree = self.stack.pop()
            elif item in '+-*/':
                # Set value
                current_tree.key = item
                # Add node to right
                current_tree.insert('', left=False)
                self.stack.append(current_tree)
                # Descend to right
                current_tree = current_tree.rhs
            else:
                # Set value
                current_tree.key = item
                # Ascend to parent
                if self.stack:
                    current_tree = self.stack.pop()
    
    def evaluate(self):
        pass

    def reset(self):
        self.root = None
        self.stack = []
    
    def validate(self, input):
        # Check only comprised of valid characters.
        # Check parentheses are matched.
        pass


def main():
    pt = ParseTree()
    pt.build('((1 + 2) + (3 + 4))')
    pt.reset()
    pt.build('3')


if __name__ == '__main__':
    main()