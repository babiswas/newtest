def count_occurance(str1):
   word_counter=dict()
   for i in list(str1):
       count=word_counter.get(i,0)
       count=count+1
       word_counter.update({i:count})
   return word_counter

if __name__=="__main__":
   print(count_occurance("Beauty lies in the eyes of beholder"))