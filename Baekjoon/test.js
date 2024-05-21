let t;
let cnt = 0;

const solution = () => {
};

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", function (input) {
  if (!t) {
    t = parseInt(input);
  }
  if (cnt == t) {
    rl.close();
  }
}).on("close", function () {
  process.exit();
});
