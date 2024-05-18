let n;
let cnt = 0;
let arr = [];

const solution = (n, arr) => {
  let rope = arr.sort((a, b) => a - b);
  let max_w = 0;
  let k = n;
  while (k > 0) {
    if (rope[n - k] * k > max_w) {
      max_w = rope[n - k] * k
    }
    k--;
  }
  console.log(max_w);
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
