line1 = input("Enter x1,x2: ").split(",")
line2 = input("Enter x3,x4: ").split(",")


def overlap(a, b):
    if (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1]):
        return "overlap"
    else:
        return "no overlap"


result1 = overlap(line1, line2)
result2 = overlap(line2, line1)
if result1 == "overlap" or result2 == "overlap":
    print("The two lines overlap")
else:
    print("The two lines do not overlap")

