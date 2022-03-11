def knapsack(arr,brr,n,W):
   if n==0 or W==0:
      return 0
   else:
     if n-1>=0:
       if arr[n-1]<=W:
          return max(knapsack(arr,brr,n-1,W),knapsack(arr,brr,n-1,W-arr[n-1])+brr[n-1])
       else:
          return knapsack(arr,brr,n-1,W)

def knapsack_dp(arr,brr,n,W,dp):
   if n==0 or W==0:
      return 0
   if dp[n][W]!=-1:
      return dp[n][W]
   else:
     if n-1>=0:
        if arr[n-1]<=W:
           dp[n][W]=max(knapsack_dp(arr,brr,n-1,W,dp),knapsack_dp(arr,brr,n-1,W-arr[n-1],dp)+brr[n-1])
           return dp[n][W]
        elif arr[n-1]>W:
           dp[n][W]=knapsack_dp(arr,brr,n-1,W,dp)
           return dp[n][W]

def knapsack_util(arr,brr,n,W):
   dp=[[-1 for i in range(W+1)] for i in range(n+1)]
   return knapsack_dp(arr,brr,n,W,dp)
   
if __name__=="__main__":
   print(knapsack([1,3,4,5],[1,4,5,7],4,7))
   print("Using memoization")
   print(knapsack_util([1,3,4,5],[1,4,5,7],4,7))

   