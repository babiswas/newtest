class Maze:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[[0 for i in range(self.vertex)] for i in range(self.vertex)]
       self.x_position=[1,-1,0,0]
       self.y_position=[0,0,1,-1]

   def find_path(self,x,y,path,visited):
       path.append((x,y))
       visited[x][y]=True
       if self.graph[x][y]==2:
          print(path)
       else:
           for i in range(4):
                x=x+self.x_position[i]
                y=y+self.y_position[i]
                if self.isSafe(x,y)==True and visited[x][y]==False:
                   self.find_path(x,y,path,visited)
           path.pop()
                         
   def find_path_in_maze(self):
       path=[]
       visited=[[False for i in range(self.vertex)] for i in range(self.vertex)]
       path=self.find_path(0,0,path,visited)
       print(path)

   def isSafe(self,x,y):
      if x<0 or x>=self.vertex:
         return False
      if y<0 or y>=self.vertex:
         return False
      if self.graph[x][y]==0:
         return False
      return True

if __name__=="__main__":
   graph=Maze(4)
   graph.graph=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,2]]
   graph.find_path_in_maze()
   
