def equal_sum_partition(arr,n):
   sum=0
   for i in arr:
      sum+=i
   if sum%2==0:
      if subset_sum(arr,n,sum//2):
         print("Equal sum partition is possible")
      else:
         print("Equal sum partition not possible")
   else:
      print("Equal sum partition not possible")

def subset_sum(arr,n,sum):
  T=[[False for i in range(sum+1)] for i in range(n+1)]
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
             T[i][j]=T[i-1][j] or T[i-1][j-arr[i-1]]
          else:
             T[i][j]=T[i-1][j]
  return T[n][sum]

if __name__=="__main__":
  equal_sum_partition([1,5,11,5],4)

        