let t;
let cnt = 0;
let p;
let n = -1;
let arr;

const solution = (p, arr) => {
  let ans = [...arr];
  let front = 0;
  let rear = ans.length;
  let del = 0;
  let reversed = false;
  for (let cur of p) {
    if (cur == "D") {
      if (ans.length - del == 0) {
        console.log("error");
        return;
      }
      del++;
      if (reversed) {
        rear -= 1;
      } else {
        front += 1;
      }
    } else {
      reversed = !reversed;
    }
  }
  ans = ans.slice(front, rear);
  let res = [];
  res.push(JSON.stringify(reversed ? ans.reverse() : ans))
  console.log(res.join('\n'));
};

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (input) {
  if (!t) {
    t = parseInt(input);
  } else if (!p) {
    p = input.split("");
  } else if (n < 0) {
    n = parseInt(input);
  } else {
    arr = input;
    if (arr != "[]") {
      arr = arr
        .replace("[", "")
        .replace("]", "")
        .split(",")
        .map((el) => +el);
    } else {
      arr = [];
    }
    solution(p, arr);
    cnt++;
    p = undefined;
    n = -1;
  }
  if (cnt == t) {
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
