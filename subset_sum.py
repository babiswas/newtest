def subset_sum(arr,n,sum):
   T=[[False for i in range(sum+1)] for j in range(n+1)]
   for i in range(n+1):
     for j in range(sum+1):
       if i==0 and j!=0:
          T[i][j]=False
       elif j==0:
          T[i][j]=True
   for i in range(1,n+1):
     for j in range(1,sum+1):
        if i-1>=0:
           if arr[i-1]<=j:
              T[i][j]=(T[i-1][j]) or (T[i-1][j-arr[i-1]])
           else:
              T[i][j]=T[i-1][j]
   return T[n][sum]

if __name__=="__main__":
   print(subset_sum([3,34,4,12,5,2],6,9))
   
    