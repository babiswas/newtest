import sys
def minm_no_coins(arr,n,W):
    if n==0 and W!=0:
       return sys.maxsize
    elif W==0:
       return 0
    else:
      if n-1>=0:
         if arr[n-1]<=W:
            return min(minm_no_coins(arr,n-1,W),minm_no_coins(arr,n,W-arr[n-1])+1)
         elif arr[n-1]>W:
            return minm_no_coins(arr,n-1,W)


if __name__=="__main__":
   print(minm_no_coins([1,2,3],3,5))
   
    