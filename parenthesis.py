def balanced_parenthesis(str1):
    stack=list()
    count=0
    for i in list(str1):
        if len(stack)==0:
          if i=='(':
            stack.append(i)
          elif i==')':
            count=count+1
        elif len(stack)!=0:
          if i=='(':
            stack.append(i)
          elif i==')' and len(stack)!=0:
            stack.pop()
    while len(stack)!=0:
        stack.pop()
        count=count+1
    return count

if __name__=="__main__":
   print(balanced_parenthesis("()())()"))
   print(balanced_parenthesis(")("))
   
  
            