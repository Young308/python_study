student_scores = input("학생들의 성적을 입력 :\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    print(student_scores)

highest_scores = 0
lowest_scores = 999
# for n in scores:
#     if (n > highest_score):
#         highest_score = n

# for n in scores:
#     if (n < lowest_score):
#         lowest_score = n

# print(f"가장 높은 점수는 : {highest_score}")
# print(f"가장 낮은 점수는 : {lowest_score}")


print(f"{max(scores)}")
print(f"{min(scores)}")
