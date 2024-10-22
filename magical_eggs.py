# Project 3 - Magical eggs and floors
# Project Members: 1. Rose Kathiravan, 2. Sneha VijayaKumar, 3. Vanday Bundu, 4. Sunil Shah
# Date: 10/21/2024

def input_eggs_number_and_floor():
    eggs = int(input("Enter the number of eggs: "))
    floors = int(input("Enter the number of floors: "))
    return eggs, floors

def magical_eggs(eggs, floors):
    #dynamic programming
    dp = [[0 for i in range(floors + 1)] for j in range(eggs + 1)]
    #linear search
    for j in range(1, floors + 1):
        dp[1][j] = j
    #dp table for all values of eggs and floors
    for i in range(2, eggs+1):
        for j in range(2, floors+1):
            dp[i][j] = float('inf')
            for k in range(1, j+1):
                worst_case = 1 + max(dp[i-1][k-1], dp[i][j-k])
                dp[i][j] = min(dp[i][j], worst_case)
    return dp[eggs][floors]

def main():
    eggs, floors = input_eggs_number_and_floor()
    min_attempts = magical_eggs(eggs, floors)
    print("The minimum number of attempts required to find the critical floor is:", min_attempts)

main()