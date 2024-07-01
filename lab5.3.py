def sum_calcu(yarn, mid_term, final):
    total = yarn + mid_term + final
    return total

def sort_s(total):
    if total > 80:
        return "ดีมาก"
    elif 50 < total <= 80:
        return "ผ่าน"
    else:
        return "ไม่ผ่าน"

def get_valid_score(prompt, max_score):
    while True:
        score = int(input(prompt))
        if score <= max_score:
            return score
        else:
            print(f"คะแนนไม่เกิน {max_score}")

yarn = get_valid_score("คะแนนเก็บ : ", 20)
mid_term = get_valid_score("คะแนนสอบกลางภาค : ", 40)
final = get_valid_score("คะแนนสอบปลายภาค : ", 40)

total_score = sum_calcu(yarn, mid_term, final)
result = sort_s(total_score)

print(f"คะแนนรวม : {total_score}")
print(f"ผลการประเมิน : {result}")