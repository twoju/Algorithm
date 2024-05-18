let n, k;
let temp = [];

const solution = (n, k, temp) => {
  let pref_sum = new Array(n);
  pref_sum[0] = temp[0]
  for (let i = 1; i < n; i++) {
    pref_sum[i] = pref_sum[i - 1] + temp[i]
  }
  let ans = pref_sum[k - 1];
  for (let i = k; i <= n; i++) {
    if (pref_sum[i] - pref_sum[i - k] > ans) {
      ans = pref_sum[i] - pref_sum[i - k]
    }
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
    [n, k] = input.split(" ").map(Number);
  } else {
    temp = input.split(" ").map((el) => +el);
    solution(n, k, temp);
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
