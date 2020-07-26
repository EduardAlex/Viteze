from mdl import UnitConversion


def locinlis(a, b):
    for i, j in enumerate(b):
        if j == a:
            return i
    return None


letters = "abcdefghijklmnopqrstuvwxyz"
v = float(input("Insert value to convert: "))
units = []
time = []

print("\n")

with open("units\\distance") as f:
    a = f.readlines()
    for e, i in enumerate(a):
        a[e] = i[:-1]
    for y, i in enumerate(a):
        b = i.split(" ")
        units.append([b[0], b[2]])
        print(letters[y], "). ", b[2])

print("\n")

with open("units\\time") as f:
    a = f.readlines()
    for e, i in enumerate(a):
        a[e] = i[:-1]
    for y, i in enumerate(a):
        b = i.split(" ")
        time.append([b[0], b[2]])
        print(y + 1, "). ", b[2])

ins = input("\nWhat speed do you want to convert from? (e.g. g6 for km/h)\n")
insd = []
res = input("\nWhat speed do you want to convert to? (e.g. d4 for m/s)\n")
resd = []

insd.append(units[locinlis(ins[0], letters)][0])
insd.append(time[int(ins[1])][0])
resd.append(units[locinlis(res[0], letters)][0])
resd.append(time[int(res[1])][0])

ucres = UnitConversion(v, insd[0], insd[1], resd[0], resd[1], "distance")

print("\n{0} {1}/{2} is equal to {3} {4}/{5}.".format(v,
                                                      insd[0], insd[1], ucres.Result, resd[0], resd[1]))
