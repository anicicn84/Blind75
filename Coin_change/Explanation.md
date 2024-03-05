## Explanation of the approach

This problem can be solved using dynamic programming, specifically using a technique often referred to as the _"Coin Change"_ problem. The idea is to build up an array that represents the number of ways to make change for amounts up to and including the target amount, using the given denominations.

### A step-by-step algorithm:

1. Initialize a DP Array: Create a one-dimensional array (`dp`) of size `amount + 1` to store the number of ways to make change for every amount from `0` to `amount`. Initialize `dp[0]` to `1` because there is exactly one way to make change for zero amount (i.e., using no coin).

2. Populate the DP Array: Iterate over each coin denomination, and for each, update the array for all amounts that can be reached by adding that denomination. For every denomination `coin`, and for every amount `x` from `coin` to `amount`, increment `dp[x]` by `dp[x - coin]`. This represents that the number of ways to make change for `x` includes all the ways to make change for `x - coin`, now including this coin.

3. Return Result: The value at `dp[amount]` will give the total number of ways to make up that amount with the given denominations.

## Time and Space Complexity

### Time Complexity
$O(N \times M)$: Where 
`N` is the total amount and `M` is the number of denominations.

- The outer loop runs for each coin denomination, a total of `M` times.
- The inner loop runs for each value from the current coin denomination up to `N`, effectively iterating `N` times in the worst case for each coin.
- Therefore, each element of the DP array is computed once per coin denomination, leading to a total of $N \times M$ computations.

### Space Complexity
O(N): Where `N` is the total amount.

- The space complexity is determined by the size of the DP array, which has `N+1` elements, where `N` is the target amount. This array is used to store the number of ways to make change for amounts from `0` to `N`.
- No additional space that scales with `N` or `M` is used, so the space complexity is linear with respect to the target amount `N`.



## Even further explanation

For every coin in `denominations`, we iterate through all possible amounts from `coin` up to `amount`. The reason for starting from `coin` is that any amount less than the current coin cannot be made up using that coin, so there's no point in considering those amounts for the current coin.

#### What happens inside the loop:

The Goal: We want to find out in how many additional ways we can achieve a total amount `x` using the current coin. We already know how many ways there are to achieve `x` without using this coin (from previous iterations or the initial state of `dp`), and now we add the ways that involve this coin.

Updating `dp[x]`: When we do `dp[x] += dp[x - coin]`, we are saying: "The number of ways to make up amount `x` includes all the ways we could make up `x` without this coin, plus all the ways we could make up `x - coin`."

Why `x - coin`? The amount `x - coin` represents what's left when we take away this coin from x. If we know how to make up `x - coin`, then by simply adding this coin to those combinations, we have found another set of ways to make up `x`.

**Example:** Suppose we have a coin of value 2 and we are calculating ways to make up the amount 5. If we already know how to make 3 (`dp[3]`), we can make 5 by adding the coin of value 2 to each of those combinations. Thus, the number of ways to make 5, which includes at least one coin of value 2, is exactly the number of ways to make 3.

This process ensures that by the time we've considered all denominations, `dp[amount]` contains the total number of ways to make up the target amount using any combination of the available coins.

The reason for adding `dp[x - coin]` to `dp[x]` rather than setting it is because there might already be other ways to make up the amount `x` with other coins considered before. This step accumulates all those possibilities, ensuring that `dp[x]` reflects the total number of distinct ways to make up an amount `x` with the given denominations up to that point in the iteration.