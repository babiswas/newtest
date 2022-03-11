class Item:
   def __init__(self,parent):
       self.parent=parent
       self.rank=0


class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=[]

   def add_edges(self,u,v):
       self.graph.append((u,v))

   def find(self,u,arr):
      while arr[u].parent!=-1:
         u=arr[u].parent
      return u

   def union(self,u,v,arr):
       index1=self.find(u,arr)
       index2=self.find(v,arr)
       if index1!=index2:
          if arr[index1].rank>arr[index2].rank:
             arr[index2].parent=index1
             arr[index1].rank+=1
          elif arr[index1].rank<arr[index2].rank:
             arr[index1].parent=index2
             arr[index2].rank+=1

   def union_find(self):
       arr=[Item(-1) for i in range(self.vertex)]
       for u,v in self.graph:
           index1=self.find(u,arr)
           index2=self.find(v,arr)
           if index1!=index2:
              self.union(u,v,arr)
           elif index1==index2:
              return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   print(graph.union_find())
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   print(graph.union_find())
              
         