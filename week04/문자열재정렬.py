"""
[문제 08: 문자열 재정렬]

알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

- 입력 조건: 
  첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

- 출력 조건: 
  첫째 줄에 문제에서 요구하는 정답을 출력합니다.
"""

import sys

s = sys.stdin.readline().strip()

#alpha는 알파벳을 담을 리스트, num은 숫자의 합을 담을 변수
alpha=[]
num=0
#숫자가 있는지 확인하기 위한 변수
has_num=False

# 문자열을 순회하며 알파벳과 숫자를 분리
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num+=int(ch)
        has_num=True

if has_num:
    # 알파벳을 오름차순으로 정렬하고, 숫자의 합과 함께 출력
    print(''.join(sorted(alpha))+str(num))
else:
    # 알파벳을 오름차순으로 정렬하고, 숫자의 합과 함께 출력
    print(''.join(sorted(alpha)))