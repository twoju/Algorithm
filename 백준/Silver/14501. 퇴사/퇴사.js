let n;
let cnt = 0;
let arr = [];

const solution = (n, arr) => {
  let ans = 0;
  const recur = (cur, tmp) => {
    if (cur >= n) {
      if (tmp > ans) {
        ans = tmp;
      }
      return;
    }
    if (cur + arr[cur][0] <= n) {
      recur(cur + arr[cur][0], tmp + arr[cur][1]);
    }
    recur(cur + 1, tmp);
  };
  recur(0, 0)
  console.log(ans)
};

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (input) {
  if (!n) {
    n = parseInt(input);
  } else {
    let [t, p] = input.split(" ").map((el) => +el);
    arr.push([t, p]);
    cnt++;
  }
  if (cnt == n) {
    solution(n, arr);
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
