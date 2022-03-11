class Node:
   def __init__(self,value):
       self.value=value
       self.right=None
       self.left=None


   def postorder(self):
      stack=list()
      root=self
      while True:
         if root:
            stack.append(root)
            root=root.left
         else:
            if not stack:
               break
            if stack[-1].right==None:
               print([node.value for node in stack])
               root=stack.pop()
               while stack[-1].right==root:
                  print([node.value for node in stack])
                  root=stack.pop()
                  if not stack:
                     break
            if stack:
               root=stack[-1].right
            else:
               break

   def inorder(self):
      if self:
         if self.left:
            self.left.inorder()
         print(self.value)
         if self.right:
            self.right.inorder()

   def insert(self,value):
      if self:
         if self.value>value:
            if self.left:
               self.left.insert(value)
            else:
               self.left=Node(value)
         elif self.value<value:
            if self.right:
               self.right.insert(value)
            else:
               self.right=Node(value)
         else:
            print("Duplicate not allowed")

if __name__=="__main__":
   node=Node(10)
   node.insert(7)
   node.insert(3)
   node.insert(5)
   node.insert(1)
   node.insert(9)
   node.insert(21)
   node.insert(15)
   node.insert(14)
   node.insert(12)
   node.inorder()
   print("Postorder traversal")
   node.postorder()
   
               