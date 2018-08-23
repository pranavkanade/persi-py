import math
if __name__ == "__main__":
    ab = int(input())
    bc = int(input())
    angle = math.degrees(math.atan(ab/bc))
    print("%d\u00b0" % round(angle))
 # round function is important. Also there is this math.ceil