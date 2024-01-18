def min_cost_jumps_bottom_up(n, k, m, cost):
    # Initialize the dynamic programming table
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    dp[0][1] = cost[0]  # Cost of the first platform

    # Array to track previous platform for each (platform, jumps) pair
    backtrack = [[-1] * (m + 1) for _ in range(n)]

    # Fill the table iteratively
    for i in range(1, n):
        for j in range(1, m + 1):
            for back in range(1, min(k + 1, i + 1)):
                prev_platform = i - back
                if dp[prev_platform][j - 1] != float('inf') and dp[prev_platform][j - 1] + cost[i] < dp[i][j]:
                    dp[i][j] = dp[prev_platform][j - 1] + cost[i]
                    backtrack[i][j] = prev_platform

    # Find the platform with the minimum cost to reach the shore
    min_cost_to_shore, last_platform = min((dp[i][m], i) for i in range(max(0, n - k), n))

    # Reconstruct the path
    path = []
    current_jump = m
    while current_jump > 0 and last_platform != -1:
        path.append(last_platform)
        last_platform = backtrack[last_platform][current_jump]
        current_jump -= 1

    return list(reversed(path))

# Main function to handle input/output
def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))

    path = min_cost_jumps_bottom_up(n, k, m, cost)

    if n<k:
      print("Error: Unable to reach the other side of the river with the given constraints.")
    else:
      for index in path:
        print(index, end=' ')

if __name__ == "__main__":
    main()
