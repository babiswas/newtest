import heapq as hq
queue=list()
pqueue=list()
hq.heapify(pqueue)


def insert_in_queue(data):
    global queue
    def get_key(k):
       return k[1]
    queue.append(data)
    queue=sorted(queue,key=get_key)

def get_data_queue():
    return queue.pop(0)

def issafe(x,y,mat):
   if x<0 or x>=len(mat):
      return False
   if y<0 or y>=len(mat):
      return False
   return True

def dkstras_algorithm(mat,start_x,start_y):
    all_visited=len(mat)*len(mat)
    visited=[[False for i in range(len(mat))] for i in range(len(mat))]
    dx=[0,1,1]
    dy=[1,1,0]
    cost=mat[start_x][start_y]
    while all_visited!=0:
        for i in range(3):
           x=start_x+dx[i]
           y=start_y+dy[i]
           if issafe(x,y,mat):
             insert_in_queue(((x,y),cost+mat[x][y]))
        queue_data=get_data_queue()
        if visited[queue_data[0][0]][queue_data[0][1]]==False:
           visited[queue_data[0][0]][queue_data[0][1]]=True
           mat[queue_data[0][0]][queue_data[0][1]]=queue_data[1]
           start_x=queue_data[0][0]
           start_y=queue_data[0][1]
        all_visited=all_visited-1
        cost=queue_data[1]
    return mat


def minimum_path(mat,start_x,start_y):
   global pqueue
   all_visited=len(mat)*len(mat)
   visited=[[False for i in range(len(mat))] for i in range(len(mat))]
   dx=[0,1,1]
   dy=[1,1,0]
   cost=mat[start_x][start_y]
   while all_visited!=0:
      for i in range(3):
         x=start_x+dx[i]
         y=start_y+dy[i]
         if issafe(x,y,mat):
            hq.heappush(pqueue,(cost+mat[x][y],(x,y)))
      qdata=hq.heappop(pqueue)
      if visited[qdata[1][0]][qdata[1][1]]==False:
         visited[qdata[1][0]][qdata[1][1]]=True
         mat[qdata[1][0]][qdata[1][1]]=qdata[0]
         start_x=qdata[1][0]
         start_y=qdata[1][1]
      all_visited=all_visited-1
      cost=qdata[0]
   return mat
         

if __name__=="__main__":
  mat=[[1,2,3],[4,8,2],[1,5,3]]
  print("simple list implementation")
  dkstras_algorithm(mat,0,0)
  print(mat)
  print(queue)
  print("priority queue implementation")
  mat=[[1,2,3],[4,8,2],[1,5,3]]
  minimum_path(mat,0,0)
  print(mat)
  print(pqueue)
  


    