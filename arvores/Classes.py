class Node:
    def __init__(self, key, left=None, right=None, father=None):
        self.father = father
        self.key = key
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None