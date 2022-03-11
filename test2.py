def knapsack_dp(arr,brr,n,W):
  T=[[-1 for i in range(W+1)] for j in range(n+1)]
  for i in range(n+1):
    for j in range(W+1):
       if i==0 or j==0:
          T[i][j]=0
  for i in range(n+1):
    for j in range(W+1):
       if i-1>=0:
          if arr[i-1]<=j:
             T[i][j]=max(T[i-1][j],T[i-1][j-arr[i-1]]+brr[i-1])
          elif arr[i-1]>j:
             T[i][j]=T[i-1][j]
  return T[n][W]

if __name__=="__main__":
   print(knapsack_dp([1,3,4,5],[1,4,5,7],4,7))