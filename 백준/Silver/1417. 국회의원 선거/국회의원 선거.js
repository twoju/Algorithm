let n;
let cnt = 0;
let arr = [];

const solution = (n, arr) => {
  let other = arr.slice(1, n);
  other.sort((a, b) => b - a);
  let dasom = arr[0];
  let ans = 0;
  while (dasom <= other[0]) {
    dasom += 1;
    other[0] -= 1;
    other.sort((a, b) => b - a);
    ans++;
  }
  console.log(ans);
};

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (input) {
  if (!n) {
    n = input;
  } else {
    arr.push(+input);
    cnt += 1;
  }
  if (cnt == n) {
    solution(n, arr);
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
