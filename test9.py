def coin_change(arr,n,W):
    if n==0 and W!=0:
       return 0
    elif W==0:
       return 1
    else:
       if n-1>=0:
         if arr[n-1]<=W:
            return coin_change(arr,n-1,W)+coin_change(arr,n,W-arr[n-1])
         else:
            return coin_change(arr,n-1,W)

if __name__=="__main__":
   print(coin_change([1,2,3],3,4))
