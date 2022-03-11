def knapsack(arr,brr,n,W):
   T=[[-1 for i in range(W+1)] for j in range(n+1)]
   for i in range(n+1):
      for j in range(W+1):
         if i==0 or j==0:
           T[i][j]=0
   for i in range(1,n+1):
      for j in range(1,W+1):
         if i-1>=0:
            if arr[i-1]<=W:
               T[i][j]=max(T[i-1][j],T[i-1][j-arr[i-1]]+brr[i-1])
            else:
               T[i][j]=T[i-1][j]
   return T[n][W]

if __name__=="__main__":
   print(knapsack([10,20,30],[60,100,120],3,50))
   
   