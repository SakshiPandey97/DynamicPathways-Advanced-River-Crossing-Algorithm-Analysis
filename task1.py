#O(k^n brute-force approach)
def find_min_cost_path(n, k, cost):
    min_cost = float('inf')
    min_cost_path = []

    def explore_path(current, path, total_cost):
        nonlocal min_cost, min_cost_path

        # Check if we can jump directly to the other side of the river
        if current + k >= n:
            if total_cost < min_cost:
                min_cost = total_cost
                min_cost_path = path.copy()
            return

        # Explore paths from the current platform to the next possible platforms
        for next_platform in range(current + 1, min(n, current + k + 1)):
            explore_path(next_platform, path + [next_platform], total_cost + cost[next_platform])

    # Start exploring paths from platform 0
    explore_path(0, [0], 0)
    return min_cost_path

def main():
    # Read the first line for n and k
    n, k = map(int, input().strip().split())

    # Read the second line for the cost array
    cost = list(map(int, input().strip().split()))

    # Find the minimum cost path
    min_cost_path = find_min_cost_path(n, k, cost)

    # Output the indices of the platforms in the minimum cost path
    for platform in min_cost_path:
        print(platform, end=' ')

if __name__ == "__main__":
    main()
