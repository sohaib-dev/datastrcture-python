import time
start_time = time.time()


def factorial(n: int) -> int:
    """ It will calculate the factorial using the recursion method.
        Factorial of large number is not recommended using the recursion because recursion limit exceed will be raised.
        :parameter
        n: positive number
    """
    if n <= 1:
        return 1
    return n*factorial(n-1)


def factorial_dp(n: int) -> int:
    """ Factorial finding using Dynamic Programming.
        :parameter
        n: positive number
    """
    dp = [1] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i
    return dp[n]


print(factorial(8)/factorial_dp(6))

print("--- %s seconds ---" % (time.time() - start_time))

