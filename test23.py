def stock_buy_sell(arr):
   n=len(arr)
   buy_index=[]
   sell_index=[]
   local_min=None
   local_max=None
   max_profit=0
   for i in range(len(arr)):
       if i<len(arr)-1 and local_min==None:
          if arr[i]<arr[i+1]:
             local_min=(arr[i],i)
       if i<len(arr)-1 and local_max==None:
         if arr[i]>arr[i+1]:
            local_max=(arr[i],i)
       if local_max and local_min:
          if local_max[1]>local_min[1]:
             buy_index.append(local_min[1])
             sell_index.append(local_max[1])
             max_profit=local_max[0]-local_min[0]
             local_max=None
             local_min=None
          else:
             local_max=None
   if len(arr)>=2:
      if arr[-1]>arr[-2]:
         local_max=(arr[-1],len(arr)-1)
      if local_min:
         buy_index.append(local_min[1])
         sell_index.append(local_max[1])
         max_profit=local_max[0]-local_min[0]
         local_max=None
         local_min=None   
   print(max_profit)
   print(buy_index)
   print(sell_index)



if __name__=="__main__":
   stock_buy_sell([100, 180, 260, 310, 40, 535, 695])




