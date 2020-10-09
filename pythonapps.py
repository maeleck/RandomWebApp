HELLO_WORLD = """
<html>
<head>
    <meta charset="UTF-8">
    <title>Find wrong translation!</title>
    <link rel="stylesheet" type="text/css" href="style.css">
<style>
body {
    background-color: #eeeeee;
}
.grid{width:600px;height:950px;margin: 0 auto;background-color: #fff;padding:10px 50px 50px 50px; border-radius:50px; border:2px solid #cbcbcb; box-shadow:10px 15px 5px #cbcbcb;
}
.grid h1{font-family:"sans-serif";background-color: #57636e;font-size:30px;text-align:center;color: #ffffff;padding:2px 0px;border-radius:50px
}
#score{color: #5A6772;text-align:center;font-size: 30px;
}
.grid #question{font-family:"monospace";font-size:60px;color: #5A6772;
}
.buttons{margin-top: 30px;
}
#btn0,#btn1,#btn2,#btn3,#btn4{background-color: #778897;width: 600px;font-size:60px;color:#fff;border:1px solid #1D3C6A;border-radius:50px;margin: 10px 40px 10px 0px;padding:10px 10px;
}

#btn0:hover,#btn1:hover,#btn2:hover,#btn3:hover,#btn4:hover{
    cursor: pointer;
    background-color: #57636e;
}
#btn0:focus,#btn1:focus,#btn2:focus,#btn3:focus,#btn4:focus{
    outline: 0;
}
#progress{color:#2b2b2b;font-size: 30px;
}
</style>
</head>
<body>
    <div class="grid">
        <div id="quiz">
            <h1>Find wrong translation! (French, German, Korean, Vietnamese, Spanish)</h1>
            <hr style="margin-bottom: 20px">

            <p id="question"></p>

            <div class="buttons">
                <button id="btn0"><span id="choice0"></span></button>
                <button id="btn1"><span id="choice1"></span></button>
                <button id="btn2"><span id="choice2"></span></button>
                <button id="btn3"><span id="choice3"></span></button>
                <button id="btn4"><span id="choice4"></span></button>
            </div>
            <hr style="margin-top: 50px">
            <footer>
                <p id="progress">Question x of y - Refresh to get new words!</p>
            </footer>

        </div>


    </div>
<script>
function Question(text, choices, answer){
    this.text = text;
    this.choices = choices;
    this.answer = answer;
}
Question.prototype.isCorrectAnswer = function (choice) {
    return this.answer === choice;
}
function Quiz(questions) {
    this.score = 0;
    this.questions = questions;
    this.questionIndex = 0;
}

//////////////////

Quiz.prototype.getQuestionIndex = function() {
    return this.questions[this.questionIndex];
}

Quiz.prototype.guess = function(answer) {
    if(this.getQuestionIndex().isCorrectAnswer(answer)) {
        this.score++;
    }

    this.questionIndex++;
}

Quiz.prototype.isEnded = function() {
    return this.questionIndex === this.questions.length;
}

////////////

function populate(){
    if(quiz.isEnded()) {
        showScores();
    }
    else {
        var element = document.getElementById("question");
        element.innerHTML = quiz.getQuestionIndex().text;

        var choices = quiz.getQuestionIndex().choices;
        for(var i=0; i< choices.length;i++){
            var element = document.getElementById("choice"+i);
            element.innerHTML = choices[i];
            guess("btn"+i, choices[i]);
        }
        showProgress();
    }
};

function guess(id, guess){
    var button = document.getElementById(id);
    button.onclick = function () {
        quiz.guess(guess);
        populate();
    }
};

function showProgress() {
    var currentQuestionNumber = quiz.questionIndex+1;
    var element = document.getElementById("progress");
    element.innerHTML= "Question "+ currentQuestionNumber+ " of "+quiz.questions.length;

};
function showScores() {
    var gameOverHTML= "<h1>Result</h1>";
    gameOverHTML+= "<h2 id='score'> Refresh to get new words! Your scores: " + quiz.score + "</h2>";
    var element = document.getElementById("quiz");
    element.innerHTML = gameOverHTML;
};

var questions1 = [
    new Question("Cat",["Katze","con meo","goyangi","chat","oro"],"oro"),
    new Question("dream",["rever","blume","kkum","mo","sueno"],"blume"),
    new Question("hope",["esperer","hoffen","gidae","mong","cara"],"cara"),
    new Question("teach",["enseigner","geduldig","galeuchida","day","ensenar"],"geduldig"),
    new Question("hurt",["blesser","verletzt","mudel","dau","herir"],"mudel"),
    new Question("east",["sur","Osten","dongjjog","phia dong","este"],"sur"),
    new Question("sleep",["sommeil","bade","jada","ngu","dormir"],"bade"),
    new Question("Wolf?",["Loup","Koch","neugdae","cho soi","lobo"],"Koch"),
    new Question("Market",["marche","Markt","sijaeng","mong","mercado"],"mong"),
    new Question("advice",["conseil","rat","joeon","pha vo","consejo"],"pha vo"),
    new Question("bite",["mordre","beissen","danjeol","can","descanso"],"descanso"),
    new Question("free",["bruyant","kostenlos","bieoissneun","mien phi","gratis"],"bruyant"),
    new Question("create",["creer","erstellen","chaengjohada","tao nen","diario"],"diario")
];

shuffleArray(questions1);

var questions = [
    questions1[0],
    questions1[1],
    questions1[2]
];


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


shuffleArray(questions[0].choices);
shuffleArray(questions[1].choices);
shuffleArray(questions[2].choices);



var quiz = new Quiz(questions);
populate();

</script>
</body>
</html>"""


#################################################################

HELLO_WORLDs = """

<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">


		<title>PCR test</title>
		<style>
.content {
  max-width: 500px;
  margin: auto;
}



.block {
  display: block;
  width: 100%;
  border: none;
  background-color: #4CAF50;
  color: white;
  padding: 14px 28px;
  font-size: 26px;
  cursor: pointer;
  text-align: center;
}

.block:hover {
  background-color: #ddd;
  color: black;
}


</style>

	</head>
	<body>
<div class="content">
	<div class="container">
		<button class="block" onclick="workClick(1)">Sequence a new virus!</button>
        <p style="text-align:center">Hint: A is complementary to T and G is complementary to C. Forward primer should match but reverse primer should be complementary and reversed with virus sequence</p>


	</div>
	<div class="container">

		Current Virus Sub-Sequence: <span id="glasses">None yet</span>
		<br>
		<br />

		<button class="block" onclick="buyFriend(1)">Design a forward primer</button>
		<br>
		<br />
		Current forward primer: <span id="friends">None yet</span>
		<br>
		<br />

		<button class="block" onclick="buyStudent(1)">Design a reverse primer</button>
		<br>
		<br />
		Current reverse primer: <span id="students">None yet</span>
		<br>
		<br />

		<button class="block" onclick="buyFactoryWorker(1)">Ampify via PCR for Diagnosis</button>

		<a href="https://en.wikipedia.org/wiki/Laboratory_diagnosis_of_viral_infections"><p style="text-align:center">How do we diagnose viral infection?</a>
		<a href="https://en.wikipedia.org/wiki/Polymerase_chain_reaction#:~:text=Polymerase%20chain%20reaction%20(PCR)%20is,in%201983%20by%20Kary%20Mullis."><p style="text-align:center">What is PCR?</a>

		<br>
		<br />
		Successful diagnosis or failure? <span id="factoryWorker"></span>
		<br />

	</div>

		<script>

	var seq = '';
    var left = '';
    var left1 = '';
    var left2 = '';
    var left3 = '';
    var leftarr = [];
var leftcomp = '';
    var leftcorrect = 'a';

    var right = '';
    var right1 = '';
    var right2 = '';
    var right3 = '';
    var rightarr = [];
var rightcomp = '';
    var rightcorrect = '';

        function makeid(length) {
   var result           = '';
   var characters       = 'AGTC';
   var charactersLength = characters.length;
   for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
   }
   return result;
}
function complement(a) {
    return { A: 'T', T: 'A', G: 'C', C: 'G' }[a];
}

function arrRan(item){
var items = item[Math.floor(Math.random() * item.length)];
return items;
}
		function workClick(number){

	seq = makeid(20);
	left = seq.substring(1, 9);

	leftcomp = left.split('').reverse().map(complement).join('');

	left1 = makeid(9);
	left2 = makeid(9);
	left3 = makeid(9);
    leftarr = [left,left1,left2,left3]

	right = seq.substring(11, 19);

	rightcomp = right.split('').reverse().map(complement).join('');


    right1 = makeid(9);
    right2 = makeid(9);
    right3 = makeid(9);
    rightarr = [right,right1,right2,right3]

    document.getElementById("glasses").innerHTML = seq ;
};



function buyFriend(number){
    leftcorrect = arrRan(leftarr);

    if (leftcorrect == left) {document.getElementById("friends").innerHTML = leftcorrect}
    else{
    document.getElementById("friends").innerHTML = leftcorrect} ;
};
function buyStudent(number){
    rightcorrect = arrRan(rightarr);

    if (rightcorrect == right) {document.getElementById("students").innerHTML = rightcomp}
    else{
    document.getElementById("students").innerHTML = rightcorrect} ;

};

function buyFactoryWorker(number){

    if (leftcorrect == left && rightcorrect == right) {
    document.getElementById("factoryWorker").innerHTML = "Success!" ;
    }
    else{
    document.getElementById("factoryWorker").innerHTML = "Failed!" ;
    }
};


		</script>

	</div>
	</body>
</html>



"""
################


HELLO_WORLDlsf= """

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Learn LSF!</title>
<style>
body {
    background-color: #fff;
}



.content {
  max-width: 800px;
  margin: auto;
}


.grid{width:800px;height:950px;margin: auto;background-color: #fff;padding:10px 50px 50px 50px; border-radius:50px; border:2px solid #cbcbcb; box-shadow:10px 15px 5px #cbcbcb;
}
.grid h1{font-family:"sans-serif";background-color: #222233;font-size:30px;text-align:center;color: #ffffff;padding:2px 0px;border-radius:50px
}
#score{color: #5A6772;text-align:center;font-size: 30px;
}
.grid #question{font-family:"monospace";font-size:60px;color: #5A6772;
}
.buttons{display: block; margin: 0 auto;
}
#btn0,#btn1,#btn2,#btn3{background-color: #222233;width: 800px;text-align: center;font-size:50px;color:#fff;border:1px solid #1D3C6A;border-radius:50px;margin: 10px 40px 10px 0px;padding:10px 10px;
}

#btn0:hover,#btn1:hover,#btn2:hover,#btn3:hover{
    cursor: pointer;
    background-color: #57636e;
}
#btn0:focus,#btn1:focus,#btn2:focus,#btn3:focus{
    outline: 0;
}
#progress{color:#2b2b2b;font-size: 30px;
}
</style>
</head>
  <body>

    <!-- 1. The <iframe> (and video player) will replace this <div> tag. -->



   <div class="grid">
        <div id="quiz">
            <h1>What are they signing in langue des signes francaise?</h1>
            <hr style="margin-bottom: 20px">




            <div id="player"></div>
            <div id="player1"></div>


            <p hidden id="question">
            </p>


            <div class="buttons">
                <button id="btn0"><span id="choice0"></span></button>
                <button id="btn1"><span id="choice1"></span></button>
                <button id="btn2"><span id="choice2"></span></button>
                <button id="btn3"><span id="choice3"></span></button>

            </div>
            <hr style="margin-top: 50px">
            <footer>
                <p hidden id="progress">Question x of y - Refresh to get new words!</p>
            </footer>

        </div>
    </div>


    <script>


function hide (elements) {
  elements = elements.length ? elements : [elements];
  for (var index = 0; index < elements.length; index++) {
    elements[index].style.display = 'none';
  }
}
function show (elements) {
  elements = elements.length ? elements : [elements];
  for (var index = 0; index < elements.length; index++) {
    elements[index].style.display = 'block';
  }
}



function Question(text, choices, answer){
    this.text = text;
    this.choices = choices;
    this.answer = answer;
}
Question.prototype.isCorrectAnswer = function (choice) {
    return this.answer === choice;
}
function Quiz(questions) {
    this.score = 0;
    this.questions = questions;
    this.questionIndex = 0;
}

//////////////////

Quiz.prototype.getQuestionIndex = function() {
    return this.questions[this.questionIndex];
}

Quiz.prototype.guess = function(answer) {
    if(this.getQuestionIndex().isCorrectAnswer(answer)) {
        this.score++;
    }

    this.questionIndex++;

}

Quiz.prototype.isEnded = function() {
    return this.questionIndex === this.questions.length;
}

////////////

function populate(){
    if(quiz.isEnded()) {
        showScores();
    }
    else {


        var element = document.getElementById("question");
        element.innerHTML = quiz.getQuestionIndex().text;

        var choices = quiz.getQuestionIndex().choices;
        for(var i=0; i< choices.length;i++){
            var element = document.getElementById("choice"+i);
            element.innerHTML = choices[i];
            guess("btn"+i, choices[i]);
        }
        showProgress();

    }
};

function guess(id, guess){
    var button = document.getElementById(id);
    button.onclick = function () {
        quiz.guess(guess);
        populate();

        hide(document.getElementById('player'));
        show(document.getElementById('player1'));
    }
};

function showProgress() {



    var currentQuestionNumber = quiz.questionIndex+1;
    var element = document.getElementById("progress");
    element.innerHTML= "Question "+ currentQuestionNumber+ " of "+quiz.questions.length;

};
function showScores() {
    var gameOverHTML= "<h1>Result</h1>";
    gameOverHTML+= "<h2 id='score'> Refresh to get new words! Your scores: " + quiz.score + "</h2> "
    ;
    var element = document.getElementById("quiz");
    element.innerHTML = gameOverHTML;
};

var questions1 = [
    new Question("dommage",["attack - attaque","avantage - advantage","ramasser - collect","dommage - pity"],"dommage - pity"),
    new Question("test",["recit - story","nombre - number","baiser - kiss","peche - peach"],"nombre - number")
];


var questions = [
    questions1[0],
    questions1[1]
];


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


shuffleArray(questions[0].choices);
shuffleArray(questions[1].choices);


var quiz = new Quiz(questions);
populate();
hide(document.getElementById('player1'));










     // 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);



      var section = {
  start: 40,
  end: 43
};

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
var player1;
function onYouTubeIframeAPIReady() {
  player = new YT.Player(
    'player',
    {
      height: '400',
      width: '800',
      videoId: 'SkduOuR4THg',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    }
  );


  player1 = new YT.Player(
    'player1',
    {
      height: '400',
      width: '800',
      videoId: 'NnJ6CmpxrkY',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    }
  );
}

function onPlayerReady(event) {

  player.seekTo(section.start);
  player.playVideo();

  player1.seekTo(section.start);

}

function onPlayerStateChange(event) {
  if (event.data == YT.PlayerState.PLAYING) {
    var duration = section.end - section.start;
    setTimeout(restartVideoSection, duration * 1000);
  }
}

function restartVideoSection() {
  player.seekTo(section.start);
  player1.seekTo(section.start);

}

    </script>
  </body>
</html>


"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins
np.random.seed(9615)

# generate df
N = 100
df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                  columns=['a', 'b', 'c', 'd', 'e'],)

# plot line + confidence interval
fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

for key, val in df.iteritems():
    l, = ax.plot(val.index, val.values, label=key)
    ax.fill_between(val.index,
                    val.values * .5, val.values * 1.5,
                    color=l.get_color(), alpha=.4)

# define interactive legend

handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                         ax.collections),
                                                     labels,
                                                     alpha_unsel=0.5,
                                                     alpha_over=1.5,
                                                     start_visible=True)
plugins.connect(fig, interactive_legend)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive legend', size=20)

""""mpld3.show()"""
html_graph = mpld3.fig_to_html(fig)
HELLO_WORLDhospital= html_graph

"""
mpld3.show()
"""





































HELLO_WORLDtoilet= """

<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">


		<title>Toilet Paper Idle Game</title>
		<style>
.content {
  max-width: 500px;
  margin: auto;
}



.block {
  display: block;
  width: 100%;
  border: none;
  background-color: #4CAF50;
  color: white;
  padding: 14px 28px;
  font-size: 26px;
  cursor: pointer;
  text-align: center;
}

.block:hover {
  background-color: #ddd;
  color: black;
}
#contentt{
  display:none;
}

#toiletcontainer {
  display:none;
  max-width: 500px;
  margin: auto;
}
#biocontainer {
  display:none;
  max-width: 500px;
  margin: auto;
}

#hospcontainer {
  display:none;
  max-width: 500px;
  margin: auto;
}
#govcontainer {
  display:none;
  max-width: 500px;
  margin: auto;
}
</style>

	</head>
	<body>
<div class="content">

		<button class="block" onclick="workClick(1)">Manufacture toilet paper to save the world! (Click here)</button>
        <p style="text-align:center">Quick, toilet paper is a hot commodity that can be sold for profit. Use the money to help push for vaccine development!</p>

		<button id="toggle">Toilet Making</button> &nbsp
		<button id="toggleBio">Bio-Lab</button> &nbsp
        <button id="toggleHosp" hidden>Hospital</button> &nbsp
        <button id="toggleGov" hidden>Government</button>

</div>

<div class="content">
<div id="toiletcontainer">
        <br> </br>
		Toilet Paper Sheet: <span id="glasses">0</span>
		<br />
		Wallet: $<span id="money">0.00</span>
		<br />
		Current Selling Price: $<span id="sellingPrice">0.50</span>
		<br />
		Toilet Paper Sheet per Tick: <span id="currentClickAmount">0</span>
        <br> </br>

        <button onclick="sellGoggles()">Sell All Toilet Paper</button>
        <br> </br>
		<button onclick="buyFriend(1)">Buy Sheet Printer</button>
		<br />
		Printer: <span id="friends">0</span> (.5 per Tick)
		<br />
		Printer Cost: $<span id="friendCost1">10</span>
		<br />

		<button onclick="buyStudent(1)">Buy Roll Assembler</button>
		<br />
		Assembler: <span id="students">0</span> (1 per Tick)
		<br />
		Assembler Cost: $<span id="studentCost">20</span>
		<br />

		<button onclick="buyFactoryWorker(1)">Buy Industrial Presser</button>
		<br />
		Presser: <span id="factoryWorker">0</span> (2 per Tick)
		<br />
		Presser: Cost: $<span id="factoryWorkerCost">110</span>
		<br />

		<button onclick="buyEnemy(1)">Modify Printers into 3D Printer</button>
		<br />
		3D Printer: <span id="enemy">0</span> (5 per Tick, -$0.10 Selling Price)
		<br />
		3D Printer Cost: <span id="enemyCost">10</span>
		<br />

		<button onclick="getContract(1)">Acquire a contract</button>
		<br />
		Contracts: <span id="contract">0</span> (Increase Selling Price by $0.20)
		<br />
		Contract Cost: <span id="contractCost">100</span>
		<br />

		<button onclick="buyClass(1)">Automate Mass Printing</button>
		<br />
		Level: <span id="classNum">0</span> (+.5 Assembler Per Tick)
		<br />
		Level Cost: $<span id="classCost">1010.00</span>
		<br />

</div>
</div>

<div class="content">
<div id="biocontainer">
        <br> </br>
        Knowledge: <span id="knowledges">0</span>
		<br />
		Reputation: <span id="reputations">0</span>
		<br />
        Toilet Paper Sheet: <span id="glasses1">0</span>
		<br />
		Wallet: $<span id="money1">0.00</span>
		<br />
		Knowledge per Tick: <span id="currentClickAmountKnowledge">0</span>
		<br />
		Reputation per Tick: <span id="currentClickAmountReputation">0</span>
        <br> </br>

		<button onclick="buyLabtech(1)">Hire a Lab Technican</button>
		<br />
		Technican: <span id="labtechs">0</span> (1 Knowledge per Tick)
		<br />
		Technican Cost: $<span id="labtechCost1">1000</span>
		<br />

		<button onclick="buyScientist(1)">Hire a Scientist</button>
		<br />
		Scientist: <span id="scientists">0</span> (2 Knowledge per Tick)
		<br />
		Scientist Cost: $<span id="scientistCost">2000</span>
		<br />

		<button onclick="buyWriter(1)">Hire a Grant Writer</button>
		<br />
		Writer: <span id="writers">0</span> (1 Reputation per Tick)
		<br />
		Writer: Cost: $<span id="writerCost">1000</span>
		<br />

		<button onclick="buyVaccine(1)">Develop Vaccine Pipeline</button>
		<br />
		Pipeline Level: <span id="vaccines">0</span> (+1 Vaccine Per Tick)
		<br />
		Cost: $<span id="vaccineCost">10000.00</span>
		<br />
		Knowledge Cost: <span id="knowCost">100</span>
		<br />
		Reputation Cost: <span id="repCost">100</span>
		<br />

</div>
</div>

<div class="content">
<div id="hospcontainer">
        <br> </br>
        PPE: <span id="glasses">0</span>
		<br />
		Healing: <span id="glasses">0</span>
		<br />
        Toilet Paper Sheet: <span id="glasses">0</span>
		<br />
		Wallet: $<span id="money">0.00</span>
		<br />
		PPE per Tick: <span id="currentClickAmount">0</span>
		<br />
		Healing per Tick: <span id="currentClickAmount">0</span>
        <br> </br>

		<button onclick="buyFriend(1)">Hire a Nurse</button>
		<br />
		Nurse: <span id="friends">0</span> (.5 Healing per Tick)
		<br />
		Nurse Cost: $<span id="friendCost1">10</span>
		<br />

		<button onclick="buyStudent(1)">Hire a Doctor</button>
		<br />
		Doctor: <span id="students">0</span> (1 Healing per Tick)
		<br />
		Doctor Cost: $<span id="studentCost">20</span>
		<br />

		<button onclick="buyFactoryWorker(1)">Hire a Specialist</button>
		<br />
		Specialist: <span id="factoryWorker">0</span> (2 Healing per Tick)
		<br />
		Specialist: Cost: $<span id="factoryWorkerCost">110</span>
		<br />

		<button onclick="getContract(1)">Improve PPE Recycling</button>
		<br />
		Recycle Level: <span id="contract">0</span> (+1 PPE Per Tick)
		<br />
		Recycle Cost: <span id="contractCost">100</span>
		<br />

		<button onclick="buyClass(1)">Adminstrate Vaccine</button>
		<br />
		Vaccinated Patient: <span id="classNum">0</span> (+1 Vaccinated Patient)
		<br />
		Cost: $<span id="classCost">1010.00</span>
		<br />


</div>
</div>

<div class="content">
<div id="govcontainer">
        <br> </br>
        Public Goodwill: <span id="glasses">0</span>
		<br />
		Cleanliness: <span id="glasses">0</span>
		<br />
        Toilet Paper Sheet: <span id="glasses">0</span>
		<br />
		Wallet: $<span id="money">0.00</span>
		<br />
		Goodwill per Tick: <span id="currentClickAmount">0</span>
		<br />
		Cleanliness per Tick: <span id="currentClickAmount">0</span>
        <br> </br>

        <button onclick="buyFriend(1)">Quarrinate</button>
		<br />
		Q. Level: <span id="friends">0</span> (1 Cleanliness per Tick)
		<br />
		Q. Level Cost: $<span id="friendCost1">10</span>
		<br />
		<button onclick="buyFriend(1)">Improve Disseminatation of Information</button>
		<br />
		Level: <span id="friends">0</span> (1 Public Goodwill per Tick)
		<br />
		Level Cost: $<span id="friendCost1">10</span>
		<br />

		<button onclick="buyStudent(1)">Improve Coordination of Emergency Supplies</button>
		<br />
		Level: <span id="students">0</span> (1 PPE per Tick)
		<br />
		Level Cost: $<span id="studentCost">20</span>
		<br />

		<button onclick="buyFactoryWorker(1)">Improve Cleansing Public Space </button>
		<br />
		Level: <span id="factoryWorker">0</span> (2 Cleaniness and 1 Public Goodwill per Tick)
		<br />
		Level: Cost: $<span id="factoryWorkerCost">110</span>
		<br />

		<button onclick="getContract(1)">Fund Vaccine Research</button>
		<br />
		Published: <span id="contract">0</span> (+.1 Knowledge Per Tick)
		<br />
		Publish Cost: <span id="contractCost">100</span>
		<br />

		<button onclick="buyClass(1)">Fund Clincial Trials</button>
		<br />
		Equipment Level: <span id="classNum">0</span> (+.1 Knowledge Per Tick)
		<br />
		Cost: $<span id="classCost">1010.00</span>
		<br />

</div>
</div>


        <div class="content">
        <br>
		Number of Vaccine Developed: <span id="vaccinedevs">0</span>
		</br>

		<p style="text-align:center">You can help yourself and your loved ones stay healthy by washing your hands often, especially during these key times when you are likely to get and spread germs or viruses.</p>


        <button onclick="saveData()">Save data</button>
        <button onclick="clearData()">Clear data</button>
        </div>

		<script>





var glasses = 0;

function workClick(number){
    glasses = glasses + number;
    document.getElementById("glasses").innerHTML = glasses;

	calculateTickAmount();
};


var money = 0;
var sellingPrice = .5;

function sellGoggles(){
	glassesAvail = Math.floor(glasses);
	money = money + glassesAvail*sellingPrice;
	glasses = glasses - glassesAvail;
	document.getElementById('money').innerHTML = money.toFixed(2);
	document.getElementById('glasses').innerHTML = glasses;
	document.getElementById('sellingPrice').innerHTML = sellingPrice.toFixed(2);
	calculateTickAmount();
};


var friends = 0;
var friendMultiplier = 1;

function buyFriend(number){
    var friendCost = Math.floor(10 * Math.pow(1.1,friends*number));     //works out the cost of this friend for number ==10
    if(money >= friendCost){                                   //checks that the player can afford the friend
        friends = friends + number;                                   //increases number of friends
    	money = money - friendCost;                          //removes the glasses spent
        document.getElementById('friends').innerHTML = friends;
        document.getElementById('money').innerHTML = money.toFixed(2);  //updates the number of glasses for the user
    };
    var nextFriend = Math.floor(10 * Math.pow(1.1,friends));       //works out the cost of the next friend
    document.getElementById('friendCost1').innerHTML = nextFriend;  //updates the cursor cost for the user
	calculateTickAmount();
};

var students = 0;
var studentMultiplier = 1;

function buyStudent(number){
    var studentCost = Math.floor(10 * Math.pow(1.2,students*number))+10;
    if(money >= studentCost){
        students = students + number;
    	money = money - studentCost;
        document.getElementById('students').innerHTML = students.toFixed(1);
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextStudent = Math.floor(10 * Math.pow(1.2,students*number))+10;       //works out the cost of the next friend
    document.getElementById('studentCost').innerHTML = nextStudent;  //updates the cursor cost for the user
	calculateTickAmount();
	//console.log(studentCost);
};

var factoryWorker = 0;
var factoryMultiplier = 1;

function buyFactoryWorker(number){
    var factoryWorkerCost = Math.floor(10 * Math.pow(1.3,factoryWorker*number))+100;
    if(money >= factoryWorkerCost){
        factoryWorker = factoryWorker + number;
    	money = money - factoryWorkerCost;
        document.getElementById('money').innerHTML = money.toFixed(2);
        document.getElementById('factoryWorker').innerHTML = factoryWorker;
    };
    var nextFactoryWorker = Math.floor(10 * Math.pow(1.8,factoryWorker))+100;       //works out the cost of the next friend
    document.getElementById('factoryWorkerCost').innerHTML = nextFactoryWorker;  //updates the cursor cost for the user
	var nextFactoryWorker10 = Math.floor(10 * Math.pow(1.8,factoryWorker*10))+100;       //works out the cost of the next friend
    document.getElementById('factoryWorkerCost10').innerHTML = nextFactoryWorker10;  //updates the cursor cost for the user
	calculateTickAmount();
	//console.log(factoryWorkerCost);
};

var enemy = 0;
var enemyMultiplier = 1;

function buyEnemy(number){
    var enemyCost = 10 * Math.pow(2,enemy);
    if(friends >= enemyCost){
        enemy = enemy + number;
    	friends = friends - enemyCost;
		sellingPrice = sellingPrice - .1;
        document.getElementById('enemy').innerHTML = enemy;
        document.getElementById('friends').innerHTML = friends;
		document.getElementById('sellingPrice').innerHTML = sellingPrice.toFixed(2);
    };
    var nextEnemy = Math.floor(10 * Math.pow(2,enemy));       //works out the cost of the next friend
    document.getElementById('enemyCost').innerHTML = nextEnemy;  //updates the cursor cost for the user
	calculateTickAmount();
	//console.log(factoryWorkerCost);
};

var classNum = 0;
function buyClass(number){
    var classCost = 10 * Math.pow(2,classNum)+1000;
    if(money >= classCost){
        classNum = classNum + number;
    	money = money - classCost;
        document.getElementById('classNum').innerHTML = classNum;
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextClass = 10 * Math.pow(2,classNum) + 1000;
    document.getElementById('classCost').innerHTML = nextClass.toFixed(2);
	document.getElementById('studentCost').innerHTML = nextStudent.toFixed(2);
	calculateTickAmount();
	//console.log(factoryWorkerCost);
};

var contract = 0;
function getContract(number){
	var contractCost = 100 * Math.pow(2, contract);
	if(glasses >= contractCost){
		contract = contract + number;
		glasses = glasses - contractCost;
		sellingPrice = sellingPrice + .2;
		document.getElementById('glasses').innerHTML = glasses;
		document.getElementById('sellingPrice').innerHTML = sellingPrice.toFixed(2);
		document.getElementById('contract').innerHTML = contract;
	};
	var contractCost = 100 * Math.pow(2, contract);
	document.getElementById('contractCost').innerHTML = contractCost;
};

var knowledges = 0;
var reputations = 0;
var vaccinedevs = 0;


function workClickKnowledge(number){
    knowledges = knowledges + number;
    document.getElementById("knowledges").innerHTML = knowledges;
	calculateTickAmount();
};

function workClickReputation(number){
    reputations = reputations + number;
    document.getElementById("reputations").innerHTML = reputations;
	calculateTickAmount();
};
function workClickVaccinedevs(number){
    vaccinedevs = vaccinedevs + number;
    document.getElementById("vaccinedevs").innerHTML = vaccinedevs;
	calculateTickAmount();
};




var labtechs = 0;
var labtechMultiplier = 1;

function buyLabtech(number){
    var labtechCost = Math.floor(1000 * Math.pow(1.1,labtechs*number));     //works out the cost of this friend for number ==10
    if(money >= labtechCost){                                   //checks that the player can afford the friend
        labtechs = labtechs + number;                                   //increases number of friends
    	money = money - labtechCost;                          //removes the glasses spent
        document.getElementById('labtechs').innerHTML = labtechs;
        document.getElementById('money').innerHTML = money.toFixed(2);  //updates the number of glasses for the user
    };
    var nextLabtech = Math.floor(1000 * Math.pow(1.1,labtechs));       //works out the cost of the next friend
    document.getElementById('labtechCost1').innerHTML = nextLabtech;  //updates the cursor cost for the user
	calculateTickAmount();
};

var scientists = 0;
var scientistMultiplier = 1;

function buyScientist(number){
    var scientistCost = Math.floor(2000 * Math.pow(1.2,scientists*number))+10;
    if(money >= scientistCost){
        scientists = scientists + number;
    	money = money - scientistCost;
        document.getElementById('scientists').innerHTML = scientists;
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextScientist = Math.floor(2000 * Math.pow(1.2,scientists*number));       //works out the cost of the next friend
    document.getElementById('scientistCost').innerHTML = nextScientist;  //updates the cursor cost for the user
	calculateTickAmount();
	//console.log(studentCost);
};

var writers = 0;
var writerMultiplier = 1;

function buyWriter(number){
    var writerCost = Math.floor(2000 * Math.pow(1.2,writers*number))+10;
    if(money >= writerCost){
        writers = writers + number;
    	money = money - writerCost;
        document.getElementById('writers').innerHTML = writers;
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextWriter = Math.floor(2000 * Math.pow(1.2,writers*number));       //works out the cost of the next friend
    document.getElementById('writerCost').innerHTML = nextWriter;  //updates the cursor cost for the user
	calculateTickAmount();
	//console.log(studentCost);
};

var publishNum = 0;
var publishMultiplier = 1;
function buyPublish(number){
    var publishCost = 10 * Math.pow(2,publishNum)+1000;
    if(money >= publishCost){
        publishNum = publishNum + number;
    	money = money - publishCost;
        document.getElementById('publishNum').innerHTML = publishNum;
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextPublish = 10 * Math.pow(2,publishNum) + 1000;
    document.getElementById('publishCost').innerHTML = nextPublish.toFixed(2);
	document.getElementById('scientistCost').innerHTML = nextScientist.toFixed(2);
	calculateTickAmount();

};

var upgradeNum = 0;
function buyUpgrade(number){
    var upgradeCost = 10 * Math.pow(2,upgradeNum)+1000;
    if(money >= upgradeCost){
        upgradeNum = upgradeNum + number;
    	money = money - upgradeCost;
        document.getElementById('upgradeNum').innerHTML = upgradeNum;
        document.getElementById('money').innerHTML = money.toFixed(2);
    };
    var nextUpgrade = 10 * Math.pow(2,upgradeNum) + 1000;
    document.getElementById('upgradeCost').innerHTML = nextUpgrade.toFixed(2);
	document.getElementById('scientistCost').innerHTML = nextScientist.toFixed(2);
	calculateTickAmount();
	//console.log(factoryWorkerCost);
};

var vaccines= 0;
var vaccineMultiplier = 1;
function buyVaccine(number){
    var vaccineCost = Math.floor(10000 * Math.pow(1.2,vaccines*number))+10;
    var knowCost = Math.floor(100 * Math.pow(1.2,vaccines*number))+10;
    var repCost = Math.floor(100 * Math.pow(1.2,vaccines*number))+10;
    if(money >= vaccineCost && knowledges >= knowCost && reputations >= repCost){
        vaccines = vaccines + number;
    	money = money - vaccineCost;
    	knowledges = knowledges - knowCost;
    	reputations = reputations - repCost;
        document.getElementById('vaccines').innerHTML = vaccines;
        document.getElementById('money').innerHTML = money.toFixed(2);
        document.getElementById('knowledges').innerHTML = knowledges;
        document.getElementById('reputations').innerHTML = reputations;

    };
    var nextVaccine = Math.floor(10000 * Math.pow(1.5,vaccines*number));       //works out the cost of the next friend
    document.getElementById('vaccineCost').innerHTML = nextVaccine;  //updates the cursor cost for the user
    var nextVaccineknow = Math.floor(200 * Math.pow(1.5,vaccines*number));       //works out the cost of the next friend
    document.getElementById('knowCost').innerHTML = nextVaccineknow;  //updates the cursor cost for the user
    var nextVaccinerep = Math.floor(200 * Math.pow(1.5,vaccines*number));       //works out the cost of the next friend
    document.getElementById('repCost').innerHTML = nextVaccinerep;  //updates the cursor cost for the user

	calculateTickAmount();
	//console.log(studentCost);
};







var clickAmount = 0;
var clickAmountKnowledge = 0;
var clickAmountReputation = 0;
var clickAmountVaccinedevs = 0
function calculateTickAmount(){

    document.getElementById("glasses1").innerHTML = glasses;
    document.getElementById("money1").innerHTML = money.toFixed(2);

	// Calculates Tick Clicks
	var friendClickAmount = friendMultiplier * friends * .5;
	var studentClickAmount = studentMultiplier * students * 1;
	var factoryClickAmount = factoryMultiplier * factoryWorker * 2;
	var enemyClickAmount = enemyMultiplier * enemy * 5;

	var labtechClickAmount = labtechMultiplier * labtechs * 1;
	var scientistClickAmount = scientistMultiplier * scientists * 2;
	var writerClickAmount = writerMultiplier * writers * 1;

	var vaccinedevsClickAmount =vaccineMultiplier * vaccines * 1;

	var clickAmount = Math.floor(friendClickAmount + studentClickAmount + factoryClickAmount + enemyClickAmount);
	var clickAmountKnowledge = Math.floor(labtechClickAmount+scientistClickAmount);
	var clickAmountReputation = Math.floor(writerClickAmount);
	var clickAmountVaccinedevs = Math.floor(vaccinedevsClickAmount);
	document.getElementById('currentClickAmount').innerHTML = clickAmount;
	document.getElementById('currentClickAmountKnowledge').innerHTML = clickAmountKnowledge;
	document.getElementById('currentClickAmountReputation').innerHTML = clickAmountReputation;
//    document.getElementById('currentClickAmountVaccinedevs').innerHTML = clickAmountVaccinedevs;
	var arrayy = [clickAmount,clickAmountKnowledge,clickAmountReputation,clickAmountVaccinedevs];

	return arrayy;
	//return(clickAmount);

};
var tickTally = 0;
window.setInterval(function(){

    var arrayy = calculateTickAmount();
	var clickAmount = arrayy[0];
	var clickAmountKnowledge = arrayy[1];
	var clickAmountReputation = arrayy[2];
	var clickAmountVaccinedevs = arrayy[3];

	workClick(clickAmount);
	workClickKnowledge(clickAmountKnowledge);
	workClickReputation(clickAmountReputation);
	workClickVaccinedevs(clickAmountVaccinedevs);

	if(classNum >= 1){
	tickTally = tickTally + 1;
	};
	if(tickTally ==10){
		tickTally = 0;
		students = students+classNum*0.1;
		document.getElementById('students').innerHTML = students;
	};
	console.log(tickTally);  //Some great logging action.
}, 1000);










































var toggle  = document.getElementById("toggle");
var toggleBio  = document.getElementById("toggleBio");
var toggleHosp  = document.getElementById("toggleHosp");
var toggleGov  = document.getElementById("toggleGov");

var contentt = document.getElementById("contentt");
var toiletcontainer = document.getElementById("toiletcontainer");
var biocontainer = document.getElementById("biocontainer");
var hospcontainer = document.getElementById("hospcontainer");
var govcontainer = document.getElementById("govcontainer");

toggle.addEventListener("click", function() {

  toiletcontainer.style.display = (biocontainer.dataset.toggled ^= 1) ? "block" : "none";

});

toggleBio.addEventListener("click", function() {
  biocontainer.style.display = (biocontainer.dataset.toggled ^= 1) ? "block" : "none"
  ;
});

toggleHosp.addEventListener("click", function() {
  hospcontainer.style.display = (hospcontainer.dataset.toggled ^= 1) ? "block" : "none"
  ;
});
toggleGov.addEventListener("click", function() {
  govcontainer.style.display = (govcontainer.dataset.toggled ^= 1) ? "block" : "none"
  ;
});








function saveData(){
    var valuee = [glasses,money,friends,students,classNum,contract, vaccines, writers, scientists, labtechs, reputations, knowledges,vaccinedevs];
    localStorage.setItem("testKey", JSON.stringify(valuee));
    alert("Your data is stored");
}


function clearData(){
    localStorage.clear();
    var valuee = [glasses=0,money=0,friends=0,students=0,classNum=0,contract=0,vaccines=0, writers=0, scientists=0, labtechs=0, reputations=0, knowledges=0, vaccinedevs=0];
    localStorage.setItem("testKey", JSON.stringify(valuee));
    alert("Your data is cleared");
}

var arrr = JSON.parse( localStorage.getItem('testKey') );
glasses = arrr[0];
money = arrr[1];
friends = arrr[2];
students = arrr[3];
classNum = arrr[4];
contract = arrr[5];


		</script>

	</div>
	</body>
</html>



"""


def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = HELLO_WORLD
    elif environ.get('PATH_INFO') == '/pcr':
        status = '200 OK'
        content = HELLO_WORLDs
    elif environ.get('PATH_INFO') == '/lsf':
        status = '200 OK'
        content = HELLO_WORLDlsf

    elif environ.get('PATH_INFO') == '/hospital':
        status = '200 OK'
        content = HELLO_WORLDhospital

    elif environ.get('PATH_INFO') == '/tps':
        status = '200 OK'
        content = HELLO_WORLDtoilet

    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')


