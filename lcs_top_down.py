def longest_common_subseq(str1,str2,m,n):
    if m==0 or n==0:
       return 0
    else:
       if str1[m-1]==str2[n-1]:
          return 1+longest_common_subseq(str1,str2,m-1,n-1)
       else:
          return max(longest_common_subseq(str1,str2,m,n-1),longest_common_subseq(str1,str2,m-1,n))

def lcs_util(str1,str2,m,n):
   T=[[-1 for i in range(n+1)] for j in range(m+1)]
   for i in range(m+1):
     for j in range(n+1):
       if i==0 or j==0:
          T[i][j]=0
   for i in range(1,m+1):
     for j in range(1,n+1):
        if i-1>=0 and j-1>=0:
          if str1[i-1]==str2[j-1]:
             T[i][j]=1+T[i-1][j-1]
          else:
             T[i][j]=max(T[i][j-1],T[i-1][j])
   return T[m][n]

def lcsget(str1,str2,m,n):
   T=[[-1 for i in range(n+1)] for j in range(m+1)]
   for i in range(m+1):
     for j in range(n+1):
       if i==0 or j==0:
          T[i][j]=0
   for i in range(1,m+1):
     for j in range(1,n+1):
        if i-1>=0 and j-1>=0:
          if str1[i-1]==str2[j-1]:
             T[i][j]=1+T[i-1][j-1]
          else:
             T[i][j]=max(T[i][j-1],T[i-1][j])
   return T

def print_lcs(str1,str2,m,n):
   T=lcsget(str1,str2,m,n)
   temp=''
   i=len(str1)
   j=len(str2)
   while (i!=0) and j!=0:
      if str1[i-1]==str2[j-1]:
         temp+=str1[i-1]
         i=i-1
         j=j-1
      elif str1[i-1]!=str2[j-1]:
         if T[i-1][j]>T[i][j-1]:
            i=i-1
         elif T[i-1][j]<T[i][j-1]:
            j=j-1
         else:
            j=j-1
   if i==0:
      while j!=0:
        temp+=str2[j-1]
        j=j-1
   elif j==0:
      while i!=0:
        temp+=str1[i-1]
        i=i-1
   return temp[::-1]


if __name__=="__main__":
   print(longest_common_subseq("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))
   print("Top down approach")
   print(lcs_util("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))
   print(print_lcs("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))