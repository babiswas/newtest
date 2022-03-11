def knapsack(arr,val,n,W):
    if n==0 or W==0:
       return 0
    elif arr[n-1]<=W:
       return max(knapsack(arr,val,n-1,W),knapsack(arr,val,n-1,W-arr[n-1])+val[n-1])
    elif arr[n-1]>W:
       return knapsack(arr,val,n-1,W)

def knap_sack_memoized(arr,val,n,W,dp):
    if n==0 or W==0:
       return 0
    if dp[n][W]!=-1:
       return dp[n][W]
    else:
       if arr[n-1]<=W:
          dp[n][W]=max(knap_sack_memoized(arr,val,n-1,W,dp),knap_sack_memoized(arr,val,n-1,W-arr[n-1],dp)+val[n-1])
          return dp[n][W]
       elif arr[n-1]>W:
          dp[n][W]=knap_sack_memoized(arr,val,n-1,W,dp)
          return dp[n][W]

def k_util(arr,val,n,W):
   dp=[[-1 for i in range(W+1)] for i in range(n+1)]
   for i in range(n+1):
       for j in range(W+1):
           if i==0 or j==0:
              dp[i][j]=0
   return knap_sack_memoized(arr,val,n,W,dp)


if __name__=="__main__":
     print(knapsack([1,3,4,5],[1,4,5,7],4,7))
     print("The memoized version of knapsack")
     print(k_util([1,3,4,5],[1,4,5,7],4,7))
     

