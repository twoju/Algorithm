"""
투포인터
-> 완탐을 해보고 투포인터로 시간을 줄여나가보기

연속 부분 수열 문제 해결을 위해 사용 (누적합 또는 투포인터)
(1 2 3 4 5 중에 2 3 4 같은 경우)

1. 조건을 만족하는 두 수
(정렬된 상태인 경우)
2. 3. 5. 7. 9. 10. 11  12
s
                        e
합이 13인걸 찾는 경우
시작s와 끝 e를 더하면 13보다 크니까 12는 제외
(e는 절대로 정답 범위에 들어올 수 없기 때문에 후보에서 제외하는 것)
(만약 합이 15인걸 찾는다면 s를 정답 범위에서 제외하고 뒤로 옮기는 것)

한칸 앞으로 당겨서 2 + 11 은 cnt+=1
sorted(map(int, input().split()))


2. 조건을 만족하는 연속된 구간

=> 맨 앞에서 같이 출발해서 구간을 늘리고 줄이는 방식
=> 슬라이딩 윈도우(s와 e 사이 간격이 같이 움직일때)

10 5
1 1 1 1 2 3 4 2 5 3 1 1 2
  i
         j => 이미 1 1 1 2 까지 왔는데 i 인덱스 움직여도 j는 그대로 있어야함. 앞으로 갈 필요 없음

for i in range(n):
	for j in range(i, n):
		if total > x:
			break
		total += ls[j]
		if total == x:
			ans += 1
=> 이렇게 하면 j가 앞으로 이동하는 불필요한 경우 발생

"""
x = 5
ls = [1, 1, 1, 1, 2, 3, 4, 2, 5, 3, 1, 1, 2]
n = len(ls)
e = 0

total = ls[0]
cnt = 0
while e < n:
	if total == x:
		cnt += 1
	if total < x:
		e += 1
		total += ls[e]
	else:
		e -= 1