#idk the time complexity is off i think something like O(n*m*log(k)) it should be log(n) the other one I have is O(k×n×m×log(n×m))
import heapq

def min_cost_jumps(n, k, m, cost):
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    dp[0][1] = cost[0]

    backtrack = [[-1] * (m + 1) for _ in range(n)]

    for jumps in range(1, m + 1):
        min_heap = []
        heapq.heappush(min_heap, (dp[0][jumps - 1], 0))

        for i in range(1, n):
            while min_heap and min_heap[0][1] < i - k:
                heapq.heappop(min_heap)

            if min_heap:
                dp[i][jumps] = min_heap[0][0] + cost[i]
                backtrack[i][jumps] = min_heap[0][1]

            heapq.heappush(min_heap, (dp[i][jumps - 1], i))

    # Find the platform with the minimum cost to reach the shore
    min_cost, last_platform = min((dp[i][m], i) for i in range(n - k, n))

    # Reconstruct the path
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
    if n<k:
        print("Error: Unable to reach the other side of the river with the given constraints.")
    else:
        for index in path:
            print(index, end=' ')

if __name__ == "__main__":
    main()