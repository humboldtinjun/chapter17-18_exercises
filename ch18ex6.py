"""exercise 6: Rewrite the body of the function using nested conditional
expressions.

This function is not very efficient because it ends up computing the same values
over and over. Make it more efficient by memoizing it, as described in Chapter 10."""

def binomial_coeff(n, k, memo={}):
    if (n, k) in memo:
        return memo[(n, k)]
    memo[(n, k)] = 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k, memo) + binomial_coeff(n-1, k-1, memo)
    return memo[(n, k)]

# Test 
print(binomial_coeff(10, 4))  # 210
print(binomial_coeff(5, 2))   # 10
print(binomial_coeff(6, 3))   # 20
print(binomial_coeff(0, 0))   # 1
print(binomial_coeff(7, 0))   # 1
