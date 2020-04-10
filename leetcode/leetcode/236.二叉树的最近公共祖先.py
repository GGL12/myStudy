class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        """
        如果以下两种情况（左子树包含p，右子树包含q/左子树包含q，右子树包含p），那么此时的根节点就是最近公共祖先
        如果左子树包含p和q，那么到root->left中继续查找，最近公共祖先在左子树里面
        如果右子树包含p和q，那么到root->right中继续查找，最近公共祖先在右子树里面
        """
        if left and right:
            return root
        elif left and not right:
            return left
        else:
            return right