#  format input:
#  >>> 1<=N<10^6, where N: int counts of employee without director
#  >>> N letter of L, where Li∈{A,B}
#  >>> 2⋅(N+1) numbers of P, where Pj 0≤Pj≤N\
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, number: int, language: set[str], parent: Optional["TreeNode"] = None):
        self.number = number
        self.language: set = language
        self.parent = parent
        self.children: set["TreeNode"] = set()

    def add_child(self, child_node: "TreeNode"):
        self.children.add(child_node)

    def has_children(self):
        return len(self.children) != 0

    def has_bearer(self):
        if not self.parent:
            return False
        return False if self.language & self.parent.language else True

    def __repr__(self):
        return "№{}{}".format(self.number, self.language)


if __name__ == '__main__':
    employee_counts = int(input().strip())
    employee_languages = tuple(input().strip().split())
    organizational_hierarchy = tuple(map(int, input().strip().split()))

    root = TreeNode(0, {"A", "B"})
    i_node = None
    for i, number in enumerate(organizational_hierarchy):

        if organizational_hierarchy[i + 1] == 0:
            i_node = root
            break
        if i == 0:
            i_node = root
            continue

        if i_node.number == number:
            i_node = i_node.parent
            continue
        else:
            new_node = TreeNode(
                number,
                {employee_languages[number - 1]},
                i_node
            )
            i_node.add_child(new_node)
            i_node = new_node

    queue = deque()
    queue.append((root, 0))
    while queue:  # O(N)
        node, bearer = queue.popleft()
        if not node.has_bearer():
            bearer = 0
        else:
            j_node = node
            while j_node.parent:  # O(root_h)
                if not j_node.parent.has_bearer():
                    if node.language & j_node.parent.language:
                        break
                    bearer += 1
                    j_node = j_node.parent
                    continue
                break
        if node.number != 0:
            print(bearer, end=" ")
        for child in node.children:
            queue.append((child, bearer))

    #  O(N*root_h)
