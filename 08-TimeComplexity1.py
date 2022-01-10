'''1부터 n까지의 합을 구하는 알고리즘1
- 합을 기록할 변수를 만들고 0을 저장
- n을 1부터 1씩 증가하면서 반복
- 반복문 안에서 합을 기록할 변수에 1씩 증가된 값을 더함
- 반복이 끝나면 합을 출력'''


def sum_all(n):
    total = 0
    for num in range(1, n+1)
    total += num
    return total

# 시간 복잡도 : O(n)
