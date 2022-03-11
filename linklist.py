def display_reverse(temp):
    if temp.next!=None:
       display_reverse(temp.next)
    print(temp.val)
       

class Node:
   def __init__(self,val):
       self.val=val
       self.next=None

   def insert(self,val):
       if self:
          temp=self
          while temp.next:
             temp=temp.next
          temp.next=Node(val)

   def display(self):
       if self:
          temp=self
          while temp:
             print(temp.val)
             temp=temp.next

   def reverse(self):
      temp=self
      curr=temp
      prev=None
      next=None
      while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
      temp=prev
      temp.display()
      return temp

   def find_middle(self):
      if self:
         temp1=self
         temp2=self
         while temp1 and temp2:
              temp1=temp1.next
              temp2=temp2.next.next
         if temp1:
            print(temp1.val)

if __name__=="__main__":
   node=Node(10)
   node.insert(13)
   node.insert(14)
   node.insert(15)
   node.display()
   print("The middle element is")
   node.find_middle()
   print("Printing the list in reverse order")
   node=node.reverse()
   print("Displaying the list using this pointer")
   node.display()
   print("Displaying in reverse order")
   display_reverse(node)