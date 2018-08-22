import sys
sys.stderr = open("error1.txt", "a")
print nosuchvar   #error gets printed in file error.txt
sys.stderr.close()
























"""
temp = sys.stderr

sys.stderr = temp  #o/p will come back to consle err
print nosuchvar


"""
