def minm_path(mat,m,n):
   T=[[-1 for i in range(len(mat))] for i in range(len(mat))]
   T[0][0]=mat[0][0]
   for i in range(1,len(mat)):
      T[i][0]=T[i-1][0]+mat[i][0]
   for j in range(1,len(mat)):
      T[0][j]=T[0][j-1]+mat[0][j]
   for i in range(1,len(mat)):
      for j in range(1,len(mat)):
         T[i][j]=mat[i][j]+min(T[i-1][j-1],T[i-1][j],T[i][j-1])
   print(T)
   return T[m][n]

def minm_path_o(mat,m,n):
   for i in range(1,len(mat)):
      mat[i][0]=mat[i-1][0]+mat[i][0]
   for j in range(1,len(mat)):
      mat[0][j]=mat[0][j-1]+mat[0][j]
   for i in range(1,len(mat)):
     for j in range(1,len(mat)):
        mat[i][j]=mat[i][j]+min(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])
   print(mat)
   return mat[m][n]


if __name__=="__main__":
   mat=[[1,2,3],[4,8,2],[1,5,3]]
   print(minm_path(mat,2,2))
   mat=[[1,2,3],[4,8,2],[1,5,3]]
   print(minm_path_o(mat,2,2))
