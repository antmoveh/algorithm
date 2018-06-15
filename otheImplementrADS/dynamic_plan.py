
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


from functools import lru_cache


@lru_cache(maxsize=128, typed=False)
def fib2(i):
    """备忘录法，自上而下"""
    if i < 2:
        return 1
    return fib2(i-1) + fib2(i-2)


def fib_iter(n):
    """迭代法，自下而上，不需要调用栈，避免了栈溢出等"""
    if n < 2:
        return 1
    a, b, c = 1, 1, 0
    while n >= 2:
        c = a + b
        a, b = b, c
        n = n - 1
    return c


"""二项式系数，递归实现"""
@lru_cache(maxsize=128, typed=False)
def cnk(n, k):
    if k == 0: return 1
    if n == 0: return 0
    return cnk(n-1, k) + cnk(n-1, k-1)


from collections import defaultdict

n, k = 10, 7
C = defaultdict(int)
for row in range(n+1):
    C[row, 0] = 1
    for col in range(1, k+1):
        C[row, col] = C[row-1, col-1] + C[row-1, col]

# 背包问题
# n=5 物品数量 c=10 书包能承受的重量 w=[2,2,6,5,4]每个物品的重量, v=[6,3,5,4,6] 每个物品价值
# 递归定义
#             0                                  if i=0 or w=0
# c[i, w] =   c[i-1, w]                          if wi > W
#             max(vi + c[i-1, w-wi], c[i-1, w])  if i>0 and w>=wi
# 自底向上实现


def bag(n, m, w, v):
    # n种物品，承重量为m，w物品的重量，v物品的价值
    # 行:承受重量 列:物品数量
    res = [[0 for j in range(m + 1)] for i in range(n + 1)]  # n+1 行，m+1列 值为0的矩阵
    for i in range(1, n + 1):
        # 迭代物品，获取当前物品和价值
        current_goods = w[i - 1]
        current_value = v[i - 1]
        for j in range(1, m + 1):
            res[i][j] = res[i - 1][j]  # 0->res[0][1]->res[1][1]
            # 如果res[i-1][j]小于res[i-1][j-w[i-1]]+v[i-1]，那么res[i][j]就等于res[i-1][j]，否则就等于res[i-1][j-w[i-1]]+v[i-1]
            # 如果承受重量大于物品重量 并且
            if j >= current_goods and res[i][j] < res[i - 1][j - current_goods] + current_value:
                res[i][j] = res[i - 1][j - current_goods] + current_value
    return res


def show(n, m, w, res):
    print("最大值为%d" % res[n][m])
    x = [False for i in range(n)]
    j = m
    for i in range(n, 0, -1):
        if res[i][j] != res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print("选择的物品为")
    for i in range(n):
        if x[i]:
            print("第%d个" % (i + 1))
    print()


if __name__ == "__main__":
    # n种物品，承重量为m，w物品的重量，v物品的价值
    m = 5
    w = [2, 1, 3, 2, 3]
    v = [12, 10, 20, 15, 2]
    n = len(w)
    res = bag(n, m, w, v)
    print(res)
    show(n, m, w, res)