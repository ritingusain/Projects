let userScore = 0;
let compScore = 0;

const choices = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");
const user_score = document.querySelector("#user-score");
const comp_score = document.querySelector("#comp-score");

const genComputerChoice = () => {
  //rock,paper,scissors
  const options = ["rock", "paper", "scissors"];
  const randIdx = Math.floor(Math.random() * 3);
  return options[randIdx];
}

const drawGame = () => {
  msg.innerText = "Game was Draw. Play Again";
  msg.style.backgroundColor ="#081b31"; 
}


const showWinner = (userWin,userChoice,compChoice) => {
  if (userWin) {
    userScore++;
    msg.innerText = `You Win! Your ${userChoice} beats ${compChoice}`;
    msg.style.backgroundColor ="green"; 
    user_score.innerText = userScore;
  }
  else {
    compScore++;
    msg.innerText = `You lost!  ${compChoice} beats your ${userChoice}`;
    comp_score.innerText =compScore;
    msg.style.backgroundColor ="red"; 
  }
}



const playGame = (userChoice) => {
  //Generate computer choice
  const compChoice = genComputerChoice();

  if (userChoice == compChoice) {
    //Draw Game
    drawGame();
  }
  else {
    let userWin = true;
    if (userChoice == "rock") {
      //scissors,paper
      userWin = compChoice === "paper" ? false : true;
    }
    else if (userChoice === "paper") {
      //rock,scissors
      userWin = compChoice === "scissors" ? false : true;
    }
    else {
      //rock,paper
      userWin = compChoice === "rock" ? false : true;
    }
    showWinner(userWin,userChoice,compChoice);
  }
}


choices.forEach((choice) => {
  choice.addEventListener("click", function () {
    const userChoice = choice.getAttribute("id");
    playGame(userChoice);
  })
})
