# 실습 문제5: Lucky 7
# 수학과 진학을 희망하는 순천이는 7의 배수를 좋아한다.
# 그래서 누군가 7의 배수를 말하면, 수넌이는 그 수를 7로 나눈 몫만큼
# 그 수를 반복해서 말한다.

num = int(input("숫자 입력: "))


if (num % 7 == 0):
    print(num*num/7)