import heapq

def min_cost_path(n, k, cost):
    # Handle cases with no platforms or a single platform
    if n == 0:
        return []
    if n == 1:
        return [0]

    # Initialize a min heap to efficiently find the platform with the minimum cost
    min_heap = [(cost[0], 0)]
    min_cost = [float('inf')] * n
    min_cost[0] = cost[0]

    # Array to store the previous platform for each platform in the path
    prev_platform = [-1] * n

    while min_heap:
        # Extract the platform with the current minimum cost
        current_cost, platform = heapq.heappop(min_heap)

        # Stop if we've reached the last platform from which we can jump to the shore
        if platform >= n - k:
            break

        # Evaluate the cost of jumping to the next platforms within jump range
        for next_platform in range(platform + 1, min(n, platform + k + 1)):
            next_cost = current_cost + cost[next_platform]
            if next_cost < min_cost[next_platform]:
                min_cost[next_platform] = next_cost
                prev_platform[next_platform] = platform
                heapq.heappush(min_heap, (next_cost, next_platform))

    # Find the last platform from which we can jump to the shore
    last_platform = n - 1
    for i in range(n - 1, n - k - 1, -1):
        if i >= 0 and min_cost[i] < min_cost[last_platform]:
            last_platform = i

    # Reconstruct the path by tracing back from the last platform
    path = []
    current = last_platform
    while current != -1:
        path.append(current)
        current = prev_platform[current]

    return list(reversed(path))

def main():
    # Read input for the number of platforms, jump length, and costs
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))

    # Find and print the path with the minimum cost
    path = min_cost_path(n, k, cost)
    for index in path:
        print(index, end=' ')

if __name__ == "__main__":
    main()
