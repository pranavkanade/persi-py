# iter.py

str = "formidable"   #str[0]

for i in str:    #for loop traverses all elements in a sequence
   print i,

print "------------------------------------------"

it = iter(str)   #iter is predenfined function

print it.next()
print it.next()
print it.next()
print "------------------------------------------"
print list(it)


'''
