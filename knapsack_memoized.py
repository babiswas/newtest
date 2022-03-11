def knapsack(arr,brr,n,W,T):
   if n==0 or W==0:
      return 0
   else:
      if T[n][W]!=-1:
         return T[n][W]
      if n-1>=0:
         if arr[n-1]<=W:
            T[n][W]=max(knapsack(arr,brr,n-1,W,T),knapsack(arr,brr,n-1,W-arr[n-1],T)+brr[n-1])
            return T[n][W]
         else:
            T[n][W]=knapsack(arr,brr,n-1,W,T)
            return T[n][W]


def knapsack_util(arr,brr,n,W):
   T=[[-1 for i in range(W+1)] for j in range(n+1)]
   knapsack(arr,brr,n,W,T)
   print(T[n][W])

if __name__=="__main__":
   knapsack_util([10,20,30],[60,100,120],3,50)
   
   
   