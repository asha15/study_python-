list = [20,30,40,50]
print(type(list))

b = bytes(list)
print(type(b))

b1 = bytearray(list)
print(type(b1))
b1[2] = 33