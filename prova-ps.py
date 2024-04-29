# Victor
# The brute force way to make this solution would've been to nest 3+ for loops.
# To garantee a lower time complexity, I used recursion.
def makeChange(n):
    # Append all possibilities to this result list
    result_list = []

    def combinations_dfs(remaining, combination, index):
        # Base case
        if index == len(coin_values):
            if remaining == 0:
                result_list.append(combination[:])
            return

        for i in range(remaining // coin_values[index] + 1):
            combination[index] = i
            # Call the function again
            combinations_dfs(remaining - i * coin_values[index], combination, index + 1)

    coin_values = [25, 10, 5, 1]
    
    # To start the recursion
    combinations_dfs(n, [0] * len(coin_values), 0)

    return result_list

n = 12
print(makeChange(n))
