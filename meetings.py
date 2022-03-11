def select_meetings(meetings):
   def get_key(meet):
       return meet[1]
   selected_meetings=list()
   meetings=sorted(meetings,key=get_key)
   selected_meetings.append(meetings.pop(0))
   for i in range(len(meetings)):
      current_meetings=meetings[i]
      if selected_meetings[-1][1]<current_meetings[0]:
         selected_meetings.append(current_meetings)
   return selected_meetings

if __name__=="__main__":
   s=[1,3,0,5,8,5]
   f=[2,4,6,7,9,9]
   meetings=list(zip(s,f))
   print(select_meetings(meetings))
   