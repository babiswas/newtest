def subset_sum(arr,n,W):
   T=[[False for i in range(W+1)] for j in range(n+1)]
   for i in range(n+1):
      for j in range(W+1):
         if j==0:
           T[i][j]=True
         elif i==0 and j!=0:
            T[i][j]=False
   for i in range(1,n+1):
      for j in range(1,W+1):
          if i-1>=0:
             if arr[i-1]<=j:
                T[i][j]=T[i-1][j] or T[i-1][j-arr[i-1]]
             elif arr[i-1]>W:
                T[i][j]=T[i-1][j]
   return T[n][W]

if __name__=="__main__":
   print(subset_sum([1,5,6,11],4,12))
   