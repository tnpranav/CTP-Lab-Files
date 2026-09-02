def knapsack_01_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            item_weight = weights[i - 1]
            item_value = values[i - 1]
            
            if item_weight <= w:
                dp[i][w] = max(
                    item_value + dp[i - 1][w - item_weight],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    selected_items.reverse()
    return dp[n][capacity], selected_items, dp


def knapsack_01_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]


if __name__ == "__main__":
    weights_1 = [2, 3, 4, 5]
    values_1 = [3, 4, 5, 6]
    capacity_1 = 5
    
    max_value_1, selected_1, dp_1 = knapsack_01_dp(weights_1, values_1, capacity_1)
    print(f"Maximum Value: {max_value_1}")
    print(f"Selected Items: {selected_1}")
    print(f"Total Weight: {sum(weights_1[i] for i in selected_1)}")
    
    weights_2 = [1, 2, 3, 4]
    values_2 = [5, 11, 15, 8]
    capacity_2 = 5
    
    max_value_2, selected_2, dp_2 = knapsack_01_dp(weights_2, values_2, capacity_2)
    print(f"\nMaximum Value: {max_value_2}")
    print(f"Selected Items: {selected_2}")
    print(f"Total Weight: {sum(weights_2[i] for i in selected_2)}")
    
    max_value_opt = knapsack_01_optimized(weights_1, values_1, capacity_1)
    print(f"\nOptimized Result: {max_value_opt}")