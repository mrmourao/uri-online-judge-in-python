import math

linha1 = input().split(" ")
linha2 = input().split(" ")

x1,y1 = linha1
x2,y2 = linha2

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

res = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("{:.4f}".format(res))