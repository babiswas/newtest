def count_subset_diff(arr,n,diff):
    sum=0
    for i in arr:
       sum+=i
    count=count_subset(arr,n,(sum+diff)//2)
    print(count)


def count_subset(arr,n,sum):
    T=[[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
      for j in range(sum+1):
         if i==0 and j!=0:
            T[i][j]=0
         elif j==0:
            T[i][j]=1
    for i in range(1,n+1):
       for j in range(1,sum+1):
          if i-1>=0:
            if arr[i-1]<=j:
               T[i][j]=T[i-1][j]+T[i-1][j-arr[i-1]]
            else:
               T[i][j]=T[i-1][j]
    return T[n][sum]

if __name__=="__main__":
   count_subset_diff([1,1,2,3],4,1)
  
    