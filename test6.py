def count_subset(arr,n,W):
   if n==0 and W!=0:
      return 0
   elif W==0:
      return 1
   else:
      if n-1>=0:
         if arr[n-1]<=W:
            return count_subset(arr,n-1,W)+count_subset(arr,n-1,W-arr[n-1])
         elif arr[n-1]>W:
            return count_subset(arr,n-1,W)


def count_subset_dp(arr,n,W):
  T=[[-1 for i in range(W+1)] for i in range(n+1)]
  for i in range(n+1):
     for j in range(W+1):
        if i==0 and j!=0:
           T[i][j]=0
        elif j==0:
           T[i][j]=1
  for i in range(1,n+1):
    for j in range(1,W+1):
      if i-1>=0:
         if arr[i-1]<=j:
            T[i][j]=T[i-1][j]+T[i-1][j-arr[i-1]]
         elif arr[i-1]>j:
            T[i][j]=T[i-1][j]
  return T[n][W]
  
  

if __name__=="__main__":
   print(count_subset([1,2,3,3],4,6))
   print("Count subset using dp")
   print(count_subset_dp([1,2,3,3],4,6))
   
   