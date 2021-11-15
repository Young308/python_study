
student_heights = input("학생들의 키를 입력하세요\n").split()
print(heights)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


total_height = 0
for height in student_heights:
    total_height += height
print(f"전체 키의 합 = {total_height}")


s
