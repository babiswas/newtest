import copy
def show_all_subset(arr,n,mylist,master_list):
    temp=copy.deepcopy(mylist)
    if temp not in master_list:
       master_list.append(temp)
    if n-1>=0:
       mylist.append(arr[n-1])
       show_all_subset(arr,n-1,mylist,master_list)
       mylist.pop()
    if n-1>=0:
       show_all_subset(arr,n-1,mylist,master_list)

if __name__=="__main__":
   master_list=list()
   show_all_subset([1,2,3,4],4,[],master_list)
   print(master_list)

        
       
        
       