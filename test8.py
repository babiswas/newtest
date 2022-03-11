def subset_sum_diff(arr,n,W):
    T=[[False for i in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
      for j in range(W+1):
         if i==0 and j!=0:
            T[i][j]=False
         elif j==0:
            T[i][j]=True
    for i in range(1,n+1):
      for j in range(1,W+1):
         if i-1>=0:
            if arr[i-1]<=j:
               T[i][j]=T[i-1][j] or T[i-1][j-arr[i-1]]
            else:
               T[i][j]=T[i-1][j]
    return T

def find_minim_subset_sum_diff(arr,n):
    max=-1
    arr_sum=sum(arr)
    T=subset_sum_diff(arr,n,arr_sum)
    for i in range(((arr_sum)//2)+1):
       if T[n][i]:
         if max<i:
            max=i
    print(max)
    return arr_sum-2*max

if __name__=="__main__":
   print(find_minim_subset_sum_diff([1,5,11,6],4))

      
       
    

