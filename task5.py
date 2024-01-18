#O(k^m) time
def find_min_cost_with_indices(current, jumps_left, total_cost, path, cost, k, n):
    if jumps_left == 0:
        if current >= n - 1:  # Can jump to the shore
            return total_cost, path
        return float('inf'), []

    min_cost = float('inf')
    min_path = []

    for next_jump in range(1, k + 1):
        next_platform = current + next_jump
        if next_platform < n:
            path_cost = total_cost + cost[next_platform]
            new_cost, new_path = find_min_cost_with_indices(next_platform, jumps_left - 1, path_cost, path + [next_platform], cost, k, n)
            if new_cost < min_cost:
                min_cost = new_cost
                min_path = new_path

    return min_cost, min_path

def main():
    n, k, m = map(int, input().split())
    cost = list(map(int, input().split()))

    _, path = find_min_cost_with_indices(0, m - 1, 0, [0], cost, k, n)  # Start from platform 0 with m-1 jumps left

    if n<k:
      print("Error: Unable to reach the other side of the river with the given constraints.")
    else:
      for index in path:
        print(index, end=' ')

if __name__ == "__main__":
    main()
