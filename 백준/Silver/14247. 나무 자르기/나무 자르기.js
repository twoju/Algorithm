let n;
let arr;
let brr;

const solution = (n, arr, brr) => {
  let ans = 0;
  let turn = brr.map((value, idx) => [value, idx]);
  turn.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < n; i++) {
    let [h, idx] = turn[i];
    ans += arr[idx] + (h * i);
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
    n = parseInt(input);
  } else if (!arr) {
    arr = input.split(" ").map((el) => +el);
  } else {
    brr = input.split(" ").map((el) => +el);
    solution(n, arr, brr);
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
