
A = ["1", "2", "3", "4", "3", "4", "2", "1", "3", "5", "1"]

# 1
A1 = []
for i in A:
    if i not in A1:
        A1.append(i)
print(A1)

# 2
A2 = list(set(A))
print(A2)

# 3
import itertools
A.sort()
A3 = []
B3 = itertools.groupby(A)
for k, g in B3:
    A3.append(k)
print(A3)

# 4
from collections import Counter
B4 = Counter(A)
A4 = list(B4.keys())
print(A4)

# 5
from collections import defaultdict
B5 = defaultdict(lambda: 0)
for i in A:
    B5[i]
A5 = list(B5.keys())
print(A5)


# 6
B6 = dict()
for i in A:
    B6.setdefault(i, 0)
A6 = list(B6)
print(A6)