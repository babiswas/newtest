class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v):
       self.graph.append((u,v))

   def find(self,u,arr):
       while arr[u]!=-1:
          u=arr[u]
       return u

   def union(self,u,v,arr):
     index1=self.find(u,arr)
     index2=self.find(v,arr)
     if index1!=index2:
        arr[index1]=index2

   def union_find(self):
       arr=[-1]*self.vertex
       for u,v in self.graph:
           index1=self.find(u,arr)
           index2=self.find(v,arr)
           if index1==index2:
              print("There is a cycle in the graph")
              return True
           elif index1!=index2:
              self.union(index1,index2,arr)
       return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   print(graph.union_find())
   graph1=Graph(4)
   graph1.add_edges(0,2)
   graph1.add_edges(0,1)
   graph1.add_edges(2,3)
   graph1.add_edges(1,3)
   print(graph1.union_find())
   


       