def circle(radius):
    area = 22/7*(radius*radius)
    return area

r = int(input("รับค่า:"))

print("พื่นที่วงกลม: %.2f" % circle(r))   