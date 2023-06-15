# input 값
nums = [3, 3, 3, 2, 2, 2]


def solution(nums):
    # 최대 N/2 만큼 가능
    max_answer = int(len(nums)/2)

    # 다른 종류의 폰켓몬이 얼마나 있는지 중복 검사하기 위한 mons
    mons = []
    # nums 가 빌 때까지 반복
    while nums:
        # mons에 포함된 종류는 제외하기
        nums = [n for n in nums if n not in mons]
        for i in nums:
            if i not in mons:
                mons.append(i)

    # 최대 데려갈 수 있는 수를 넘는지 아닌지 확인
    if len(mons) >= max_answer:
        answer = max_answer
    else:
        answer = len(mons)
    return answer


# 간결한 풀이가 있어서 놀랐는데 일단 내 코드에 적용할 수 있는 방법은
#   if len(mons) >= max_answer:
#       answer = max_answer
#   else:
#       answer = len(mons)
# 이 코드를
#   min(max_answer, len(mons))
# 이렇게 줄여서 작성할 수 있다.

# 또 다른 방법은 중복 검사를 일일히 해주지 않아도,
# set(nums) 를 이용해서 간단하게 해줄 수 있다.
# set() 은 집합 자료형으로 중복을 허용하지 않고, 순서가 없다(Unordered).

print(solution(nums))
