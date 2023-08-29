// input
const nums = [3, 3, 3, 2, 2, 2]

// 첫번째 방법
// 중복을 없애주는 uniq 를 만들어서 최솟값을 비교한다.
// 다른 풀이를 보니 비슷하지만 Set()에 직접 nums 를 넣어도 가능했다.

// function solution(nums) {
//     var answer = 0;
//     var max_answer = nums.length / 2
//     const uniq = array => [...new Set(array)]
//     answer = Math.min(max_answer, uniq(nums).length)
//     return answer;
// }

function solution(nums) {
    var answer = 0;
    const max_answer = nums.length / 2
    const mons = [...new Set(nums)]
    answer = Math.min(max_answer, mons.length)
    return answer;
}

console.log(solution(nums))