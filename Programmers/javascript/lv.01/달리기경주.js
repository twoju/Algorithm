var players = ["mumu", "soe", "poe", "kai", "mine"]
const callings = ["kai", "kai", "mine", "mine"]

function solution(players, callings) {
    var answer = [];
    callings.map((player, i) => {
        var index = players.index 
        console.log(player)
        players[index], players[index - 1] = players[index - 1], players[index]
    });
    answer = players;
    return answer;
}