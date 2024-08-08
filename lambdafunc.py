#city=["lahore", "karachi", "islamabad", "sahiwal"]
#def length(city):
 #   return len(city)
#sort= sorted(city, key=length)
#print("sorted cities by word length: ", sort)


city=["lahore", "karachi", "islamabad", "sahiwal"]
sort= sorted(city, key=lambda x: len(x))
print("sorted cities by word length: ",sort)