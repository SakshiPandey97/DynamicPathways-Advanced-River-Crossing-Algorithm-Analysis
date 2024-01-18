from collections import deque

def min_cost_jumps(n, k, m, cost):
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    dp[0][1] = cost[0]

    backtrack = [[-1] * (m + 1) for _ in range(n)]

    for jump in range(1, m + 1):
        deq = deque([(dp[0][jump - 1], 0)])

        for i in range(1, n):
            while deq and deq[0][1] < i - k:
                deq.popleft()

            dp[i][jump] = deq[0][0] + cost[i]
            backtrack[i][jump] = deq[0][1]

            while deq and deq[-1][0] >= dp[i][jump - 1]:
                deq.pop()

            deq.append((dp[i][jump - 1], i))

    # Reconstruct the path
    min_cost, last_platform = min((dp[i][m], i) for i in range(n))
    path = []
    current_jump = m
    while current_jump > 0 and last_platform != -1:
        path.append(last_platform)
        last_platform = backtrack[last_platform][current_jump]
        current_jump -= 1

    return list(reversed(path))

def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))

    path = min_cost_jumps(n, k, m, cost)

    # Check if the path only contains the starting platform
    if path == [0]:
        print("Error: Unable to reach the other side of the river with the given constraints.")
    else:
        for index in path:
            print(index, end=' ')

if __name__ == "__main__":
    main()

