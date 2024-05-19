let t;
let cnt = 0;
let arr = [];

const solution = (arr) => {
  let n = arr.length;
  let stack = [];
  let ans;
  for (let i = 0; i < n; i++) {
    if (arr[i] == "(") {
      stack.push(arr[i]);
    } else {
      if (stack[stack.length - 1] == "(") {
        stack.pop();
      } else {
        ans = "NO";
      }
    }
    if (ans) break;
  }
  if (!ans) {
    if (stack.length === 0) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  } else {
    console.log(ans);
  }
};

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (input) {
  if (!t) {
    t = parseInt(input);
  } else {
    let vps = input.split("");
    arr = vps;
    solution(arr);
    cnt++;
  }
  if (cnt == t) {
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
