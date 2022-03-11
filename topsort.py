from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=defaultdict(list)

    def add_edges(self,u,v):
        self.graph[u].append(v)


    def topsort_util(self,stack,visited,u):
        print(stack)
        visited[u]=True
        for i in self.graph[u]:
          if not visited[i]:
             self.topsort_util(stack,visited,i)
        stack.append(u)

    def top_sort(self):
        stack=list()
        visited=[False for i in range(self.vertex)]
        for i in range(self.vertex):
          if not visited[i]:
             self.topsort_util(stack,visited,i)
        while stack:
          print(stack.pop())

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(4,0)
   graph.add_edges(5,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,0)
   graph.add_edges(4,3)
   graph.top_sort()
        