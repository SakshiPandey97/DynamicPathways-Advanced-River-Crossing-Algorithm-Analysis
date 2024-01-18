from collections import deque

def min_cost_path(n, k, cost):
    # Special cases for 0 or 1 platform
    if n == 0:
        return []
    if n == 1:
        return [0]

    # Initialize the minimum cost array
    min_cost = [float('inf')] * n
    min_cost[0] = cost[0]

    # Use a deque to efficiently find the minimum cost within the jump range
    q = deque([0])

    # Store the previous platform for each platform
    prev_platform = [-1] * n

    # Calculate the minimum cost for each platform
    for i in range(1, n):
        # Remove platforms from the deque that are out of the jump range
        while q and q[0] < i - k:
            q.popleft()

        # Update the minimum cost for the current platform
        min_cost[i] = min_cost[q[0]] + cost[i]
        prev_platform[i] = q[0]

        # Maintain the deque to store platforms with the minimum cost
        while q and min_cost[i] <= min_cost[q[-1]]:
            q.pop()
        q.append(i)

    # Find the last platform from which we can jump to the shore
    last_platform = n - 1
    for i in range(n - 1, n - k - 1, -1):
        if i >= 0 and min_cost[i] < min_cost[last_platform]:
            last_platform = i

    # Reconstruct the path by tracing back from the last platform
    platforms = []
    i = last_platform
    while i >= 0:
        platforms.append(i)
        i = prev_platform[i]

    return list(reversed(platforms))

def main():
    # Read input for the number of platforms, jump length, and costs
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))

    # Find and print the path with the minimum cost
    platforms = min_cost_path(n, k, cost)
    for platform in platforms:
        print(platform, end=' ')

if __name__ == "__main__":
    main()
