def min_cost_path(n, k, cost):
    # Memoization table to store the minimum cost and previous platform for each platform
    memo = [(-1, -1)] * n

    # Recursive function to compute the minimum cost and previous platform for platform i
    def dp(i):
        if i == 0:
            return cost[0], -1
        if memo[i][0] != -1:
            return memo[i]

        min_cost = float('inf')
        prev_platform = -1
        for j in range(max(0, i - k), i):
            current_cost, _ = dp(j)
            current_cost += cost[i]
            if current_cost < min_cost:
                min_cost = current_cost
                prev_platform = j

        memo[i] = (min_cost, prev_platform)
        return memo[i]

    # Find the minimum cost to reach the shore (or beyond)
    min_cost_to_shore = float('inf')
    last_platform = -1
    for i in range(n - k, n):
        current_cost, _ = dp(i)
        if current_cost < min_cost_to_shore:
            min_cost_to_shore = current_cost
            last_platform = i

    # Reconstruct the path
    path = []
    while last_platform != -1:
        path.append(last_platform)
        _, last_platform = memo[last_platform]

    return list(reversed(path))

def main():
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))

    path = min_cost_path(n, k, cost)
    for platform in path:
        print(platform, end=' ')

if __name__ == "__main__":
    main()
