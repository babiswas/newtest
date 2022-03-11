class A:
   def __init__(self,a):
      self.a=a
   def __iter__(self):
       return self
   def __next__(self):
       if not hasattr(A,'b'):
          self.b=4
       if self.a>self.b:
          raise StopIteration
       item=self.a
       self.a=self.a+1
       return item

if __name__=="__main__":
   a=A(1)
   obj=iter(a)
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
  