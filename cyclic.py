from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def is_cyclic_util(self,recstack,visited,u):
       recstack[u]=True
       visited[u]=True
       for i in self.graph[u]:
         if not visited[i]:
            if self.is_cyclic_util(recstack,visited,i):
               return True
         elif recstack[i]==True:
              return True
       return False

   
   def is_cyclic(self):
       recstack=[False for i in range(self.vertex)]
       visited=[False for i in range(self.vertex)]
       for i in range(self.vertex):
         if not visited[i]:
            if self.is_cyclic_util(recstack,visited,i):
               return True
       return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   print(graph.is_cyclic())

       