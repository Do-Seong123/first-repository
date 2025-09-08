score = int(input("성적을 입력하시오 : "))

if score >= 90:
    rank = "A"
elif 90 > score >= 80:
    rank = "B"
elif 80 > score >= 70:
    rank = "C"
elif 70 > score >= 60:
    rank = "D"
else:
    rank = "F"

print(f"{rank}학점입니다.")