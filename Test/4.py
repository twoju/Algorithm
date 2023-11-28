coin = 3
cards = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]

from collections import deque

def solution(coin, cards):
    n = len(cards)
    total = n // 3

    my_card = cards[:total]

    def check(arr):
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[i] + arr[j] == n + 1:
                    ans += 1
        return ans

    if coin == total:
        return total + 1
    elif coin == 0:
        return check(my_card)
    else:
        cnt = 0
        q = deque()

        for i in cards[total:]:
            q.append(i)

        def recur(cur, c, arr, q):
            nonlocal cnt

            if cur > 0 and check(arr) == 0:
                cnt = max(cnt, cur)
                return
            if cur == n - total + 1:
                print(cur)
                cnt = max(cnt, cur)
                return
            if c == 0:
                cur += check(arr)
                cnt = max(cnt, cur)
                return
            if len(q) == 0:
                cnt = max(cnt, cur)
                return
            
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    if arr[i] + arr[j] == n + 1:
                        del arr[j]
                        del arr[i]
            
            a = q.popleft()
            b = q.popleft()

            recur(cur + 1, c, arr[:], q)
            a_arr = arr + [a]
            recur(cur + 1, c - 1, a_arr, q)
            b_arr = arr + [b]
            recur(cur + 1, c - 1, b_arr, q)
            ab_arr = arr + [a, b]
            recur(cur + 1, c - 2, ab_arr, q)


        recur(0, coin, my_card, q)
        
        return cnt
    
print(solution(coin, cards))