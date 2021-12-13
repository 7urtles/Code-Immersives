// -----[ Game Settings ]-----
const size = 20
const height = size
const width = size
const boardSize = height * width
let movementDirection = 1
let gameSpeed = 250 // Lower is faster?
let level = 1
const Http = new XMLHttpRequest();
const url='http://charlesparmley.tech/scores';
const urlPost='http://charlesparmley.tech/scoresUpdate';
const goalSound= new Audio('http://charlesparmley.tech/Snake/goal.mp3')
let highScore = 10
let highScoreMinimum = 100


//  -----[ Game Setup ]-----

// constructs a game square when called
let createSquare = () =>{
    let square = document.createElement('div')
    square.classList.add('gameSquare')
    return square
}

// Builds the board using specified settings
let createBoard = (boardSize) =>{
    const board = document.getElementById('board')
    board.style.height = 'max-content';
    board.style.width = `${size+3}rem`;
    board.style.padding = '1rem'
    board.style.flexDirection = 'row';
    board.style.justifyContent = 'center';
    board.style.margin = 'auto';
    board.style.boxShadow = '5px 5px 5px black'
    board.style.marginTop = '5rem'

    for(i=0;i<boardSize;i++){
        let square = createSquare()
        square.id = i
        document.getElementById('board').append(square)
    }
}

// Places goal square on the board
let createGoal = (boardSize) =>{
    // picks a random square on the board
    const goal = Math.floor(Math.random() * boardSize)
    goalSquare = document.getElementById(goal)
    // and now it is food
    goalSquare.classList.add('goalSquare')
}

// Creates the initial snake head node
let createSnakeHead = () =>{
    let snakeHead = document.getElementById(parseInt(boardSize*.5))
    snakeHead.classList.add('snakeHead')
    return
}

// increase length of snake
let growSnake=()=>{
    level++
}
// The plan for implimenting body movement is to leave the previously moved to square the same
//   color as the snake, for a number of turns equal to the snakes length value
let moveSnake=(oldHead,newHead)=>{
    
    // remove head from old square
    oldHead.classList.remove('snakeHead')
    // place on new square
    newHead.classList.add('snakeHead')
    // place body piece on old head location
    oldHead.classList.add('snakeBody')

    // set the how long it will last using the 'level' setting as a timer starting number
    oldHead.setAttribute('value', level)
    
    // Array containing all existing body sections of the snake
    let snakeBody = document.getElementsByClassName('snakeBody')

    // for every section of the body
    for(let i=0;i<snakeBody.length;i++){
        // save section to variable
        let section = snakeBody.item(i)
        // get the value of it's existing timer
        let timer = parseInt(section.getAttribute('value'))
        // if there is still time on the timer
        if(timer > 0){
            // lower the timer by 1
            timer--
            // and update the section with the new timer value
            section.setAttribute('value', timer)
        }
    }
    return
}
//checking for collision with edge of map
let collisionChecker=(newLocation,movementDirection)=>{
    // look our location on the map
    newLocation = parseInt(newLocation)
    // On an edge piece, and moving away from map center, OR on a snake body piece
    //      Then we have LOST
    if((newLocation % width === 0 & movementDirection === 1) || ((newLocation+1) % width === 0 & movementDirection === -1) || newLocation > boardSize || newLocation < 0 || document.getElementById(String(newLocation)).classList.contains('snakeBody') === true){
        // If score is in the top 3 scores
        if((level-1) > highScoreMinimum){
            // Prompt user to submit name to leaderboard
            let userName = window.prompt('High Score! Enter Name!')

            // Post request. If you are reading this, here is where you would cheat....
            // Please don't. Doing so will delete valid high scores and I would rather not
            //  put forth the effort to write a workaround... 
            // Hope you have enjoyed so far!
            console.log(userName)
            if(userName != null){
                $.ajax(urlPost, {
                    type: 'POST',
                    url: urlPost,
                    dataType: "json",
                    data: {
                        user : userName,
                        score : level-1
                    },
                    success: function(){
                        // console.log('Success')
                    },
                    error: function(){
                        // console.log('Failure')
                    }
                });
            }
        }
        // Ask user to play again, and show their score.
        if(confirm(`Score: ${level-1}    Play Again?`)===true){
            // if user clicks to play again, reload the page
            location.reload()
        }
        else{ 
            // if the do not 'play again', 
            //   returning true signals the parent loop to cancel
            return true
        }
    }
}

// Create game scoreboard
let createScoreboard =()=>{
    // create board html element
    let scoreboard = document.createElement('div')
    scoreboard.className = 'scoreboard'

    // add style for scoreboard
    scoreboard.classList.add('scoreboard')
    scoreboard.style.display = 'flex'
    scoreboard.style.justifyContent = 'center'
    // create score counter element
    let scoreCounter = document.createElement('h2')
    // set counter to current level
    scoreCounter.innerText = `Score: ${level-1}`
    scoreCounter.id = 'currentScore'
    // add it to the DOM
    scoreboard.appendChild(scoreCounter)
    board.appendChild(scoreboard)
}

// Create leaderboard
let initialized = false
let createLeaderboard=(data=[])=>{
    // Check if this has already happened
    if (initialized === true){
        // if so, dont recreate the leaderboard
        return
    }
    let parsedData = data
    // if the data is not a js object
    if(typeof(parsedData)!='object'){
        // parse it into one
        parsedData = JSON.parse(parsedData)
    }

    // I don't remember why I did this....
    // Why would it matter if the data was longer than 30 or less than one?
    // If leaderboard gets weird ------!!! BUG HERE !!!-----
    // if(parsedData.length>30 || data.length < 1){
    //     return
    // }


    let leadearboard = document.getElementById('leaderboard')
    // loop over leaderboard data
    for(i=0;i<parsedData.length;i++){
        // create a div for each one
        let userScore = document.createElement('div')
        userScore.className = 'leaderScore'

        // finding the minimum high score needed for leaderboard
        //    again, no cheating please. I'll emojify this whole thing
        if(parsedData[i].score < highScoreMinimum){
            highScoreMinimum = parsedData[i].score
        }

        // Grabbing user data from data supplied
        username = parsedData[i].user
        score = parsedData[i].score

        // Giving their respective elements identifying attributtes
        userScore.id = parsedData[i].user
        userScore.setAttribute('value', parsedData[i].score)

        // creating element and giving it the username and score
        let scoreText = document.createElement('p')
        scoreText.innerText = `${username}: ${score}`

        // flatten the elements to the leaderboard
        userScore.appendChild(scoreText)
        leadearboard.appendChild(userScore)
    }

    
    // loop a dictionary of scores kept in a local json file,
    // use the data per username to display high scores
    initialized = true
}



// Updates scoreboard value when needed    Example: snake reaches food piece
let updateScoreboard =()=>{
    let currentScore = document.getElementById('currentScore')
    currentScore.innerText = `Score: ${level-1}`
    board.removeChild(board.lastChild);
    createScoreboard()
}


// Run setup functions
createBoard(boardSize)
createGoal(boardSize)
createSnakeHead(boardSize)
createScoreboard()



// -----[ Game Runtime ]-----
runtime=()=>{
    // check the current date down to the millisecond, minus the gamespeed (also milliseconds)
    let expected = Date.now() - gameSpeed;
    setTimeout(tick, gameSpeed);
    function tick() {

        let dt = Date.now() - expected; // the drift (positive for overshooting)
        if (dt > gameSpeed) {
            // if more time has occurred than specified by gamespeed
        }

        // -----[ Game Main Loop ]-----
        // goal location
        let goal = document.getElementsByClassName('goalSquare')[0]
        let goalLocation = goal.id

        // location of snake head
        let oldHead = document.getElementsByClassName('snakeHead')[0]
        // ID from it's division
        let location = parseInt(oldHead.id)
        // initializing new location
        let newLocation = '0'

        // find new location
        newLocation = String(parseInt(oldHead.id) + movementDirection)
        // grab division id of new location
        newHead = document.getElementById(newLocation)

        // Check for wall collision
        if (collisionChecker(newLocation,movementDirection)===true){
            return
        }

        // Move the snake
        moveSnake(oldHead,newHead)


        // Without this, snake poops sometimes. And they are literally deadly
        // Checks if any snakeBody elements have a value of '0'
        // If so remove the class snakeBody from it
        let snakeBody = document.getElementsByClassName('snakeBody')
        for(let i=0;i<snakeBody.length;i++){
            let section = snakeBody.item(i)
            let timer = parseInt(section.getAttribute('value'))
            if(timer < 1){
                section.removeAttribute('value')
                section.classList.remove('snakeBody')
                section.classList.remove('snakeTail')
                section.classList.remove('right','left','up','down')
            }
        }
        // If reached a food piece square
        if (newLocation === goalLocation){
            goalSound.play()
            // remove the goal
            goal.classList.remove('goalSquare')
            // place a new one
            createGoal(boardSize)
            // enlarge snake by 1
            growSnake()
            // update html scoreboard DOM element
            updateScoreboard()
            // increace framerate by decreasing delay between snake movements
            gameSpeed = gameSpeed*.9 // multiplying by .9 increases the game speed by 10%
        }

        // Set time when next game tick is allowed
        expected += gameSpeed;

        // IDK yet, still tyring to understand
        setTimeout(tick, Math.max(0, gameSpeed - dt)); // take into account drift
    }
}


// -- Movement Listener --
$(document).keydown(function(event){
    // [ KEY PRESSES ]
    switch (event.which){
        case 37: // LEFT
            movementDirection = -1
            break;

        case 38: // UP
            movementDirection = -width
            break;      
          
        case 39: // RIGHT
            movementDirection = 1
            break;

        case 40: // DOWN
            movementDirection = width
            break;
    }
});

Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
    const data = Http.response 
    createLeaderboard(data)
}


  
// Run Game
runtime()
