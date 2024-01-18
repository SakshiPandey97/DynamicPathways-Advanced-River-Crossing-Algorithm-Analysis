def find_min_cost_with_indices(current, jumps_left, total_cost, path, cost, k, n, memo):
    if jumps_left == 0:
        if current >= n - 1:  # Can jump to the shore
            return total_cost, path
        return float('inf'), []

    if memo[current][jumps_left] is not None:
        return memo[current][jumps_left]

    min_cost = float('inf')
    min_path = []

    for next_jump in range(1, k + 1):
        next_platform = current + next_jump
        if next_platform < n:
            path_cost = total_cost + cost[next_platform]
            new_cost, new_path = find_min_cost_with_indices(next_platform, jumps_left - 1, path_cost, path + [next_platform], cost, k, n, memo)
            if new_cost < min_cost:
                min_cost = new_cost
                min_path = new_path

    memo[current][jumps_left] = (min_cost, min_path)
    return min_cost, min_path

def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))

    memo = [[None for _ in range(m + 1)] for _ in range(n)]
    _, path = find_min_cost_with_indices(0, m - 1, 0, [0], cost, k, n, memo)

    if n<k:
      print("Error: Unable to reach the other side of the river with the given constraints.")
    else:
      for index in path:
        print(index, end=' ')

if __name__ == "__main__":
    main()
