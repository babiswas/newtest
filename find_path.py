def is_safe(matrix,x,y,l):
    if x<0 or x>=l:
       return False
    if y<0 or y>=l:
       return False
    if matrix[x][y]==0:
       return False
    return True

def find_path(matrix,x,y,visited,l,path):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    path.append((x,y))
    visited[x][y]=True
    if matrix[x][y]==2:
       return True
    else:
      for i in range(4):
         X=x+dx[i]
         Y=y+dy[i]
         if is_safe(matrix,X,Y,l) and visited[X][Y]==False:
            if find_path(matrix,X,Y,visited,l,path):
               return True
      path.pop()
    return False

def find_path_util(matrix,start_x,start_y):
    visited=[[False for i in range(len(matrix))] for i in range(len(matrix))]
    path=list()
    if find_path(matrix,start_x,start_y,visited,len(matrix),path):
       print(path)
       print(f"The path from {start_x},{start_y} to destination is possible")
    else:
       print(f"The path from {start_x},{start_y} to destination is not possible")
    

if __name__=="__main__":
   matrix=[[0,3,2],[3,3,0],[1,3,0]]
   find_path_util(matrix,2,0)
   
    
    
    
    