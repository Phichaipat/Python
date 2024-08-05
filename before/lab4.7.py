def BMI():
    result = G / (H / 100)**2
    return result

G = int(input("น้ำหนัก: "))
H = int(input("ส่วนสูง: "))

BMI_R = BMI() 

print("BMI = %.2f" % BMI_R)

if BMI_R < 18.50:
    print("น้ำหนักน้อย/ผอม")
    print("ภาวะเสี่ยงต่อโรค: มากกว่าปกติ")
elif BMI_R >= 18.50 and BMI_R <= 22.90:
    print("ปกติ(สุขภาพดี)")
    print("ภาวะเสี่ยงต่อโรค: เท่าคนปกติ")
elif BMI_R >= 23 and BMI_R <= 24.90:
    print("ท้วม/โรคอ้วนระดับ1")
    print("ภาวะเสี่ยงต่อโรค: อันตรายอันดับ1")
elif BMI_R >= 25 and BMI_R <= 29.90:
    print("อ้วน/โรคอ้วนระดับ2")
    print("ภาวะเสี่ยงต่อโรค: อันตรายอันดับ2")
elif BMI_R >= 30:
    print("อ้วนมาก/โรคอ้วนระดับ3")
    print("ภาวะเสี่ยงต่อโรค: อันตรายอันดับ3")
