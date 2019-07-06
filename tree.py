class TreeNode():
    def __init__(self, rule, probability, left=None, right=None):
        self.rule = rule
        self.left = left
        self.right = right
        self.probability = probability
