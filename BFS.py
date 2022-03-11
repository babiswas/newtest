from collections import defaultdict

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def BFS(self,u):
       queue=[]
       visited=[False]*self.vertex
       queue.append(u)
       visited[u]=True
       while queue:
          m=queue.pop(0)
          print(m)
          for i in self.graph[m]:
            if not visited[i]:
               visited[i]=True
               queue.append(i)

   def print_levels(self,u):
       queue=list()
       visited=[False]*self.vertex
       queue.append(u)
       visited[u]=True
       while queue:
          q_len=len(queue)
          if q_len!=0:
             print(queue)
             while q_len:
                m=queue.pop(0)
                for i in self.graph[m]:
                   if visited[i]==False:
                      queue.append(i)
                      visited[i]=True
                q_len=q_len-1

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.BFS(2)
   print("Enter through different points")
   for i in range(graph.vertex):
       print(f"enter through the point {i}")
       graph.BFS(i)
   print("Level order traversal of the directed graph")
   graph.print_levels(2)

          