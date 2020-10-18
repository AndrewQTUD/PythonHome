//Keeping track of the score and other related variables.
const userScore = 0;
const computerScore = 0;
const userScore_span = document.getElementById("user-score");
const computerScore_span = document.getElementById("computer-score");
const scoreBoard_div = document.querySelector(".score-board");
const result_div = document.querySelector(".result");
const rock_div = document.getElementById("r");
const paper_div = document.getElementById("p");
const scissor_div = document.getElementById("s");

function getCompChoice() {
  const choices = ["r", "p", "s"];
  const randNum = Math.floor(Math.random() * 3);
  return choices[randNum];
}

function game(userChoice) {
  const compChoice = getCompChoice();
  switch (userChoice + compChoice) {
    case "rs":
      console.log("[USER WINS.]");
    case "pr":
      console.log("[USER WINS.]");
    case "sp":
      console.log("[USER WINS.]");
  }
}

function main() {
  rock_div.addEventListener("click", function () {
    game("Rock");
  });

  paper_div.addEventListener("click", function () {
    game("Paper");
  });

  scissor_div.addEventListener("click", function () {
    game("Scissors");
  });
}

main();
