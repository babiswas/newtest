def subset_sum(arr,n,sum):
    T=[[-1 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
      for j in range(sum+1):
         if i==0 or j!=0:
            T[i][j]=False
         elif j==0:
            T[i][j]=True
    for i in range(1,n+1):
       for j in range(1,sum+1):
          if i-1>=0:
             if arr[i-1]<=j:
                T[i][j]=T[i-1][j] or T[i-1][j-arr[i-1]]
             else:
                T[i][j]=T[i-1][j]
    return T


def minm_subset_sum_diff(arr,n):
   max=-99999
   sum=0
   for i in arr:
      sum+=i
   T=subset_sum(arr,n,sum)
   temp=T[n]
   for i in range((sum//2)+1):
     if temp[i]==True:
        if max<i:
           max=i
   return abs(sum-2*max)

if __name__=="__main__":
   print(minm_subset_sum_diff([1,6,11,5],4))
   
       
     
   
   