#
#   @description:
#   On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.)
#   If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3.
#   ( if n % 3 == 0 , then n = n / 3  ). Now the question is, given a positive integer n, find the minimum number of steps
#   that takes n to 1 eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )    3.)
#   For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )
#   @author: Hayden McParlane
import math

def find_min_steps():
    n = 11
    print(min_steps(n))

def min_steps(n):
    dp = list([0, 0])
    # Zero indexing in python means that each iteration is considering
    # desired_value - 1. Therefore, algorithm corrects that.
    for i in range(n):
        b = c = float('+inf')
        a = dp[i]
        if is_divisable_by(2, i + 1):
            b = dp[int((i + 1) / 2)]
        if is_divisable_by(3, i + 1):
            c = dp[int((i + 1) / 3)]
        dp.append(min(a, b, c) + 1)
    return dp[n - 1]

def is_divisable_by(divisibility_factor, number):
    return number % divisibility_factor is 0

if __name__ == "__main__":
    find_min_steps()