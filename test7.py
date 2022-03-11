def subset_sum(arr,n,W):
    T=[[-1 for i in range(W+1)] for j in range(n+1)]
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

def subset_sum_diff(arr,n,diff):
    sum_arr=sum(arr)
    return subset_sum(arr,n,(sum_arr+diff)//2)


if __name__=="__main__":
   print(subset_sum_diff([1,2,3,2,4],5,2))
   
