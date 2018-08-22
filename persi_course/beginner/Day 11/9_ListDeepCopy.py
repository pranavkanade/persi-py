import copy       #copy is  a pre defined module
listOne = [[1, 'hello'],[2, 'world']]
newlist =listOne        #shallow copy
print "listOne = ", listOne                 #listOne =  [[1, 'hello'], [2, 'world']]
print "newlist = ", newlist                 #newlist =  [[1, 'hello'], [2, 'world']]
print "id of listOne = ", id(listOne)       #id of listOne =  50857416
print "id of newlist = ", id(newlist)       #id of newlist =  50857416
print "------------------------------------------------------------"
listTwo = copy.deepcopy(listOne)        #deepcopy() method of copy module used to obtain deep copy of the object #creating a new container but containing references to completely new copies (references)print "listTwo = ", listTwo             #listTwo =  [[1, 'hello'], [2, 'world']]
print "id of listOne = ", id(listOne)   #id of listOne =  50857416
print "id of listTwo = ", id(listTwo)   #id of newlist =  50529736
print "------------------------------------------------------------"
listOne.append(500)
print "Changed listOne =", listOne      #Changed listOne = [[1, 'hello'], [2, 'world'], 500]
print "UnChanged listTwo =", listTwo    #UnChanged listTwo = [[1, 'hello'], [2, 'world']]
print "------------------------------------------------------------"
tupleTwo = tuple(listTwo)               #you to create a tuple from a existing list by using tuple() function
print "Tuple Two = ",tupleTwo
l1 = list(tupleTwo)
print "List l1 = ", l1


num = 100
print "num = ", type(num)
num = "ABC"
print "num = ", type(num)


print "tupleTwo = ", type(tupleTwo)







