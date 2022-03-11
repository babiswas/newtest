def subset_sum(arr,n,W):
   if n==0 and W!=0:
      return False
   elif W==0:
      return True
   else:
      if n-1>=0:
         if arr[n-1]<=W:
            return subset_sum(arr,n-1,W) or subset_sum(arr,n-1,W-arr[n-1])
         elif arr[n-1]>W:
            return subset_sum(arr,n-1,W)

if __name__=="__main__":
   print(subset_sum([1,5,6,11],4,12))