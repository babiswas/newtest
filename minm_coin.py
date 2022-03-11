import sys
def minm_no_coins(arr,n,sum):
   T=[[-1 for i in range(sum+1)] for j in range(n+1)]
   for i in range(n+1):
     for j in  range(sum+1):
        if i==0 and j!=0:
           T[i][j]=sys.maxsize
        elif j==0:
           T[i][j]=0
   for j in range(1,sum+1):
      if j%arr[0]==0:
         T[1][j]=j//arr[0]
      else:
         T[1][j]=sys.maxsize
   for i in range(2,n+1):
     for j in range(1,sum+1):
       if i-1>=0:
          if arr[i-1]<=j:
             T[i][j]=min(T[i-1][j],T[i][j-arr[i-1]]+1)
          else:
             T[i][j]=T[i-1][j]
   return T[n][sum]

if __name__=="__main__":
   print(minm_no_coins([1,2,3],3,5))
        