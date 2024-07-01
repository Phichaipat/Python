num_people = int(input("โปรดระบุจำนวนคน: "))
scores = []

for i in range(num_people):
    score = int(input(f"โปรดระบุคะแนนของนักเรียน {i + 1}: "))
    scores.append(score)

total_score = sum(scores)
average_score = total_score / num_people

print(f"คะแนนเฉลี่ย {num_people} คน คือ :", average_score)

