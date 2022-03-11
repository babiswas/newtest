def longest_common_subseq(str1,str2,m,n):
    if m==0 or n==0:
       return 0
    else:
       if str1[m-1]==str2[n-1]:
          return 1+longest_common_subseq(str1,str2,m-1,n-1)
       else:
          return max(longest_common_subseq(str1,str2,m,n-1),longest_common_subseq(str1,str2,m-1,n))

if __name__=="__main__":
   print(longest_common_subseq("abcdgh","abedfhr",len("abcdgh"),len("abedfhr")))
   