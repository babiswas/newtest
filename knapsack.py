def knapsack(arr,brr,n,W):
   if n==0 or W==0:
      return 0
   else:
      if n-1>=0:
         if arr[n-1]<=W:
            return max(knapsack(arr,brr,n-1,W),knapsack(arr,brr,n-1,W-arr[n-1])+brr[n-1])
         else:
            return knapsack(arr,brr,n-1,W)

if __name__=="__main__":
   print(knapsack([10,20,30],[60,100,120],3,50))
