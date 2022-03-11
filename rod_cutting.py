def rod_cutting(arr,cost,n,l):
    if l==0 or n==0:
       return 0
    else:
       if n-1>=0:
         if arr[n-1]<=l:
            return max(rod_cutting(arr,cost,n-1,l),rod_cutting(arr,cost,n-1,l-arr[n-1])+cost[n-1])
         else:
            return rod_cutting(arr,cost,n-1,l)

if __name__=="__main__":
   print(rod_cutting([1,2,3,4,5,6,7,8],[1,5,8,9,10,17,17,20],8,8))
  