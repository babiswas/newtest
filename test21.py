import sys
def min_path(mat,m,n,T):
   if m<0 or n<0 or m>=len(mat) or n>=len(mat):
      return sys.maxsize
   if T[m][n]!=-1:
      return T[m][n]
   else:
      if m==0 and n==0:
         T[m][n]=mat[m][n]
         return T[m][n]
      else:
         T[m][n]=mat[m][n]+min(min_path(mat,m-1,n,T),min_path(mat,m-1,n-1,T),min_path(mat,m,n-1,T))
         return T[m][n]


def min_path_util(mat,m,n):
  T=[[-1 for i in range(len(mat)+1)] for i in range(len(mat)+1)]
  path=min_path(mat,m,n,T)
  return path

if __name__=="__main__":
   mat=[[1,2,3],[4,8,2],[1,5,3]]
   print(min_path_util(mat,2,2))
  