const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
];

const usernames = [];
const winners = [];
let sum_sc = 0;

gameInfo.forEach((item, i, arr) => {
    usernames.push(item.username);
    sum_sc += parseInt(item.score);
})

gameInfo.forEach((item, i, arr) => {
    if (item.score > 5) {
        winners.push(item.username);
    }
})

console.log(usernames);
console.log(winners);
console.log(sum_sc);

