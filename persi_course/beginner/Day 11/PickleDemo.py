import pickle
a=100
b="PSL"
c=[3.1456,'x','y']
file = open("state.txt", 'w')
pickle.dump(a, file)    #saves the Python objects in some pickle string foramt
pickle.dump(b, file)
pickle.dump(c, file)
file.close()
print"----------------------------------------------------"

file = open("state.txt", 'r')
a1 = pickle.load(file)
b1 = pickle.load(file)
c1 = pickle.load(file)
print "a1= ",a1
print "b1= ",b1
print "c1= ",c1
file.close()
