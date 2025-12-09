from __future__ import annotations
from typing import Optional, Tuple


class TreeNode:
    """Simple binary tree node."""
    def __init__(self, value: int,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Return True if the binary tree rooted at `root` is height-balanced.
    """

    def check(node: Optional[TreeNode]) -> Tuple[bool, int]:
        if node is None:
            return True, 0

        left_balanced, left_height = check(node.left)
        right_balanced, right_height = check(node.right)

        balanced = (
            left_balanced
            and right_balanced
            and abs(left_height - right_height) <= 1
        )
        height = 1 + max(left_height, right_height)
        return balanced, height

    balanced, _ = check(root)
    return balanced