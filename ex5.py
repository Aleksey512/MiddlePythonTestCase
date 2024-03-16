#  format input:
#  >>> 1<=N<=3*10^5, where N: int counts of arrays
#  ... for i in N
#  >>>  1<=k<=3⋅10^5, where k size of array
#  >>>  k integers of aij, where 1<=aij<=109
# ...
#
from collections import defaultdict


def closeness(list_indexes, depth=0):
    step = defaultdict(list)
    for i in list_indexes:
        if len(arrays[i]) > depth:
            step[arrays[i][depth]].append(i)
    r_sum = 0
    for x in step.values():
        if len(x) > 1:
            r_sum = len(x) * (len(x) - 1) // 2 + closeness(x, depth + 1)
    return r_sum


if __name__ == "__main__":
    array_counts = int(input())
    arrays = []
    for i in range(array_counts):
        array_size = int(input())
        array = list(map(int, input().strip().split()))
        arrays.append(array)

    print(closeness(list(range(array_counts))))

    # nearest = 0
    # for i, array_i in enumerate(arrays):
    #     for array_j in arrays[i+1:]:
    #         if array_i == array_j:
    #             nearest += len(array_i)
    #             continue
    #         k = 1
    #         while array_i[:k] == array_j[:k]:
    #             nearest += 1
    #             k += 1
    # print(nearest)
