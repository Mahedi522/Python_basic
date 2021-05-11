
f = open("L_V.gif", "rb")

f1 = open("lv.jpg", "wb")

for pic in f:
    f1.write(pic)