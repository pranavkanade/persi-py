x=100
z=3.45  #no data type 
y='Hello'
#print "Started"
#y=y+1   run time error no concatenation of int to str object
if z==3.45 or y=='Hello':
    x =x+1
    y=y+' World'   #+ is concatenation operator
else:
    print 'In else block'
print "x = ",x
print 'y = \t value',y

print "-------------------------------------------------"
print """a'b"c"""     """xyz'm"a"""
print int(z)
print float(x)
print "Kinght's"     "abc'z"
print 'Kinght"s'    'abc"z'
#try except
#print x+"AAAA"    #not poosible  GIVES U run time error TypeError
#raw string
print 'c\temp\new.txt'  #\t and \n escape charaters are resolved
print r'c\temp\new.txt'    #raw string   it considers this as raw string as it is
str1 = r'c\temp\new.txt'
print "str1 = ", str1