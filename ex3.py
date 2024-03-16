#  input format:
#  >>> N M Q, where N - row, M - column, Q - count limits
#           and 1<=NxM<=3*10^5; 1<=Q<=10^5
#  >>> M elements of L, where 1<=L<=10
#  ...
#  >>> N rows of M, where -10^9<=aij<=10^9
#  ...
#  ...
#  >>> Q rows of L, q, val, where qk∈(<,>); -10^9<=val<=10^9
from typing import NamedTuple, Literal

MATCHING_METHOD = {
    '>': "__gt__",
    "<": "__lt__",
}


class Action(NamedTuple):
    column_name: str
    q: Literal["<", ">"]
    val: int


def get_action_from_input(input_string: str) -> Action:
    column_name, q, val = input_string.split()
    return Action(column_name, q, int(val))


if __name__ == "__main__":
    N, M, Q = map(int, input().split())
    columns = {name: i for i, name in enumerate(input().split())}

    table = tuple(list(map(int, input().split())) for _ in range(N)) #  [[], [], []]

    constraints = tuple(get_action_from_input(input()) for _ in range(Q))

    valid_rows = set(range(N))
    for constraint in constraints:  # O(Q)
        index = columns[constraint.column_name]
        valid_rows = {
            row_index for row_index in valid_rows if  # O(N)
            getattr(
                table[row_index][index],
                MATCHING_METHOD[constraint.q])(constraint.val)
        }

    total_sum = sum(sum(row) for i, row in enumerate(table) if i in valid_rows)  # O(N^2)

    print(total_sum)

    # O(N^2)
