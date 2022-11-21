# 1.py

# n = int(input("Enter the # of seq val: "))
# def recur(n):
#     if n<=1:return n
#     return recur(n-1) + recur(n-2)
# for i in range(n):
#     print(recur(i))

# def iterative(n):
#     fib = [0,1]
#     if n > 1:
#         for i in range(2, n+1):
#             fib.append(fib[i-1]+fib[i-2])
#     elif n == 1: return 0
#     elif n == 2: return fib
#     return fib
# print(iterative(n))

# print("*"*100)

# 2.py
# string = 'A'*3+'B'*4+'C'*2+'D'*6+'E'*4
# from collections import defaultdict
# from heapq import heapify, heappush, heappop

# dt = defaultdict(int)
# for i in string:
#     dt[i] += 1

# heap = [[weight, [symbol, '']] for symbol, weight in dt.items()]
# heapify(heap)
# while len(heap) > 1:
#     l = heappop(heap)
#     r = heappop(heap)
#     for val in l[1:]:
#         val[1] += '0'
#     for val in r[1:]:
#         val[1] += '1'
#     heappush(heap, [l[0]+r[0]]+l[1:]+r[1:])
# print(heap)
# for val in heap[0][1:]:
#     print(val[0], val[1][::-1])

# 3.py
# val = [3, 4, 5, 6]
# wt = [2, 3, 4, 5]
# V = 5
# n = len(val)

# def knap(V, wt, val, n):
#     dp = [[0 for _ in range(V+1)] for _ in range(n+1)]

#     for i in range(n+1):
#         for w in range(V+1):
#             if i == 0 or w == 0:
#                 dp[i][w] = 0
#             elif wt[i-1] <= w:
#                 dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
#             else:
#                 dp[i][w] = dp[i-1][w]
    
#     return dp[n][V]
# print(knap(V, wt, val, n))

# 4.py
# N = 5
# x,y = 3,2 
# cnt = 0
# board = [[0]*N for _ in range(N)]
# def iscorrect(row, col):
#     for i in range(row):
#         if board[i][col]:
#             return False
    
#     i = row
#     j = col
#     while i >= 0 and j >= 0:
#         if board[i][j]:
#             return False
#         i -= 1
#         j -= 1
#     i = row
#     j = col
#     while i >= 0 and j < N:
#         if board[i][j]:
#             return False
#         i -= 1
#         j += 1
#     return True

# def display():
#     global cnt
#     if board[x][y]:
#         cnt += 1
#         for i in range(N):
#             print(board[i])
#         print('\n')

# def nqueens(row):
#     if row == N:
#         display()
#         return True
#     chk = False
#     for i in range(N):
#         if iscorrect(row, i):
#             board[row][i] = 1
#             chk = nqueens(row+1)
#             board[row][i] = 0
#     return chk

# nqueens(0)

# 5.py
data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
quicksort(data, 0, size-1)
print(data)