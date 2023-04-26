const question = document.getElementById("question");
const choices = Array.from(document.getElementsByClassName("choicetext"));
const progressText = document.getElementById("progresstext");
const scoreText = document.getElementById("score");
const progressBarFull = document.getElementById("progressbarfull");

let currentQuestion = {};
let acceptingAnswers = true;
let score = 0;
let questionCounter = 0;
let availableQuestions = [];

let questions = [
  {
    question: "Inside which HTML element do we put the JavaScript??",
    choice1: "<script>",
    choice2: "<javascript>",
    choice3: "<js>",
    choice4: "<scripting>",
    answer: 1,
  },
  {
    question:
      "What is the correct syntax for referring to an external script called 'xxx.js'?",
    choice1: "<script href='xxx.js'>",
    choice2: "<script name='xxx.js'>",
    choice3: "<script src='xxx.js'>",
    choice4: "<script file='xxx.js'>",
    answer: 3,
  },
  {
    question: " How do you write 'Hello World' in an alert box?",
    choice1: "msgBox('Hello World');",
    choice2: "alertBox('Hello World');",
    choice3: "msg('Hello World');",
    choice4: "alert('Hello World');",
    answer: 4,
  },
  {
    question: "Which of the following is not an input device for a computer? ",
    choice1: " Keyboard",
    choice2: "Monitor",
    choice3: "Mouse",
    choice4: "Scanner",
    answer: 2,
  },
  {
    question: "What is the purpose of a firewall?",
    choice1: "To protect the computer from viruses ",
    choice2: "To prevent unauthorized access to the computer",
    choice3: "To increase the speed of the computer",
    choice4: "To improve the quality of the computer's display",
    answer: 2,
  },
  {
    question: "What is the purpose of a graphical user interface (GUI)?",
    choice1: "To provide a command line interface for advanced users",
    choice2:
      "To provide a text-based interface for users with visual impairments",
    choice3:
      "To provide an intuitive and user-friendly way to interact with software",
    choice4: "To provide a way for multiple users to share the same computer",
    answer: 3,
  },
  {
    question:
      "Which of the following is a programming language used for web development?",
    choice1: "Java",
    choice2: "Python",
    choice3: "HTML",
    choice4: "C++",
    answer: 3,
  },
  {
    question: " How many golden rules are there?",
    choice1: "6",
    choice2: "9",
    choice3: "0",
    choice4: "8",
    answer: 4,
  },
];

const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 3;

startGame = () => {
  questionCounter = 0;
  score = 0;
  availableQuestions = [...questions];
  console.log(availableQuestions);
  getNewQuestion();
};

getNewQuestion = () => {
  if (availableQuestions.length === 0 || questionCounter >= MAX_QUESTIONS) {
    localStorage.setItem("mostRecentScore", score);
    return window.location.assign("/end");
  }
  questionCounter++;
  progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;

  progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`;

  const questionIndex = Math.floor(Math.random() * availableQuestions.length);
  currentQuestion = availableQuestions[questionIndex];
  question.innerText = currentQuestion.question;

  choices.forEach((choice) => {
    const number = choice.dataset["number"];
    choice.innerText = currentQuestion["choice" + number];
  });

  availableQuestions.splice(questionIndex, 1);

  acceptingAnswers = true;
};

choices.forEach((choice) => {
  choice.addEventListener("click", (e) => {
    if (!acceptingAnswers) return;

    acceptingAnswers = false;
    const selectedChoice = e.target;
    const selectedAnswer = selectedChoice.dataset["number"];

    const classToApply =
      selectedAnswer == currentQuestion.answer ? "correct" : "incorrect";

    if (classToApply === "correct") {
      incrementScore(CORRECT_BONUS);
    }

    selectedChoice.parentElement.classList.add(classToApply);

    setTimeout(() => {
      selectedChoice.parentElement.classList.remove(classToApply);
      getNewQuestion();
    }, 1000);
  });
});

incrementScore = (num) => {
  score += num;
  scoreText.innerText = score;
};

startGame();
