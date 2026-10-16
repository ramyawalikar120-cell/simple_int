import sys

def simpleInt(p, intr, time):
    return (p * intr * time) / 100

if _name_ == "_main_":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])
    print("Simple Interest =", simpleInt(p, i, t))