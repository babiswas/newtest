import copy
def display(l):
    l=[str(i) for i in l]
    print(" ".join(l))

def pascals_triangle(n):
   state=[1,1]
   current=list()
   if n==1:
      print(1)
   elif n==2:
      print(1)
      print(" ".join(["1","1"]))
   else:
      print(1)
      print(" ".join(["1","1"]))
      n=n-2
      while n:
        start=0
        current.append(1)
        for i in state:
           if start!=len(state)-1:
              current.append(sum(state[start:start+2]))
              start=start+1
           else:
              break
        current.append(1)
        display(current)
        state=copy.deepcopy(current)
        current.clear()
        n=n-1

if __name__=="__main__":
   pascals_triangle(7)
   

        
      
      