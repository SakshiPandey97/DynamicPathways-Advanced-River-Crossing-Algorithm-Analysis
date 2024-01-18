from collections import deque

def min_cost_path(n, k, cost):
    if n == 0:
        return []
    if n == 1:
        return [0]

    min_cost = [float('inf')] * n
    min_cost[0] = cost[0]
    prev_platform = [-1] * n
    q = deque([0])

    for i in range(1, n):
        while q and q[0] < i - k:
            q.popleft()

        min_cost[i] = min_cost[q[0]] + cost[i]
        prev_platform[i] = q[0]

        while q and min_cost[i] <= min_cost[q[-1]]:
            q.pop()
        q.append(i)

    last_platform = -1
    min_cost_to_shore = float('inf')
    for i in range(n - 1, n - k - 1, -1):
        if i >= 0 and min_cost[i] < min_cost_to_shore:
            min_cost_to_shore = min_cost[i]
            last_platform = i

    path = []
    current = last_platform
    while current != -1:
        path.append(current)
        current = prev_platform[current]

    return list(reversed(path))

# Main Function to Handle Input/Output
def main():
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))

    path = min_cost_path(n, k, cost)
    for index in path:
        print(index, end=' ')

if __name__ == "__main__":
    main()
