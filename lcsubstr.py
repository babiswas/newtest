def longest_common_sub(str1,str2,m,n,length):
    T=[[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
      for j in range(n+1):
        if i==0 or j==0:
           T[i][j]=0
           if length<T[i][j]:
              length=T[i][j]
    for i in range(1,m+1):
       for j in range(1,n+1):
           if str1[i-1]==str2[j-1]:
              T[i][j]=1+T[i-1][j-1]
              if length<T[i][j]:
                 length=T[i][j]
           else:
              T[i][j]=0
              if length<T[i][j]:
                 length=T[i][j]
    return length

def longest_common_substr(str1,str2,m,n,length):
    if m==0 or n==0:
       return 0
    else:
       if str1[m-1]==str2[n-1]:
          temp1=1+longest_common_substr(str1,str2,m-1,n-1,length)
          if length<temp1:
             length=temp1
          return length
       else:
          temp2=max(longest_common_substr(str1,str2,m-1,n,0),longest_common_substr(str1,str2,m,n-1,0))
          if temp2>length:
             length=temp2
          return length


if __name__=="__main__":
   length=-99999
   print(longest_common_sub("abcdxyz","xyzabcd",len("abcdxyz"),len("xyzabcd"),length))
   print("recursive")
   print(longest_common_substr("abcdxyz","xyzabcd",len("abcdxyz"),len("xyzabcd"),length))


          