from itertools import islice

def remove_duplicates(l):
   s=set()
   for i in l:
     s.add(i)
   l=list(s)
   return l

def get_lists(l):
  master_list=list()
  it=iter(l)
  k=list(islice(iter(l),2))
  master_list.append(k)
  while True:
     k=list(islice(it,2))
     if not k:
        break
     else:
       master_list.append(k)
  return master_list



if __name__=="__main__":
   l=[1,1,2,2,3,3,4,4,6,7,8]
   print(remove_duplicates(l))
   print(get_lists([1,2,3,4,5,6,7,8,9,10]))
