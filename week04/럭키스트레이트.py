"""
[문제 07: 럭키 스트레이트] 

게임의 아웃복서 캐릭터는 필살기인 '럭키 스트레이트' 기술이 있습니다. 
이 기술은 매우 강력한 대신에 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있습니다.

특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 
왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미합니다.

예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1 + 2 + 3, 
오른쪽 부분의 각 자릿수의 합은 4 + 0 + 2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있습니다.

현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하세요.

- 입력 조건: 
  첫째 줄에 점수 N이 정수로 주어집니다. (10 <= N <= 99,999,999) 
  단, 점수 N의 자릿수는 항상 짝수 형태로만 주어집니다.

- 출력 조건: 
  첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"를 출력합니다.
"""

import sys

n = sys.stdin.readline().strip()

#짝수 자릿수이므로 절반 길이 계산 무조건 자연수
half_length = len(n) // 2

# 왼쪽 부분과 오른쪽 부분의 각 자릿수 합 구하기
left_sum=0
left_part = n[:half_length]
for ch in left_part:
    left_sum += int(ch)
right_sum=0
right_part = n[half_length:]
for ch in right_part:
    right_sum += int(ch)

# 조건 비교 후 결과 출력
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")


# 왼쪽 부분과 오른쪽 부분의 각 자릿수 합 구하기
# left_sum = sum(int(ch) for ch in n[:half_length])
# right_sum = sum(int(ch) for ch in n[half_length:])

