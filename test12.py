import sys
def minm_coins(arr,n,W):
    T=[[-1 for i in range(W+1)]for i in range(n+1)]
    for i in range(n+1):
      for j in range(W+1):
         if i==0 and j!=0:
            T[i][j]=sys.maxsize-1
         elif j==0:
            T[i][j]=0
    for i in range(1,W+1):
       if i%arr[0]==0:
          T[1][i]=i//arr[0]
       else:
          T[1][i]=sys.maxsize-1
    for i in range(2,n+1):
      for j in range(1,W+1):
         if i-1>=0:
            if arr[i-1]<=j:
               T[i][j]=min(T[i-1][j],T[i-1][j-arr[i-1]]+1)
            elif arr[i-1]>j:
               T[i][j]=T[i-1][j]
    return T[n][W]


if __name__=="__main__":
   print(minm_coins([1,2,3],3,5))
   

          
        