//  TODO

// Create grid for game - DONE

// Create goal square - DONE

// Create snake head - DONE

// Snake movement - DONE(Manual mode only)

// Snake goal capture

// Goal respawn

// Snake growth

// Multi-segment snake movement



// -----[ Game Settings ]-----

const height = 8
const width = 8
const boardSize = height * width
let snakeDirection = 1
let level = 1


//  -----[ Game Setup ]-----

// constructs a game square when called
let createSquare = () =>{
    let square = document.createElement('div')
    square.classList.add('gameSquare')
    square.style.boxShadow = '5px 5px 5px black'
    return square
}

// Builds the board using specified settings
let createBoard = (boardSize) =>{
    const board = document.getElementById('board')
    board.style.height = '25rem';
    board.style.width = '25rem';
    board.style.display = 'flex';
    board.style.flexDirection = 'row';
    board.style.flexWrap = 'wrap';
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
    const goal = Math.floor(Math.random() * boardSize)
    goalSquare = document.getElementById(goal)
    goalSquare.classList.add('goalSquare')
}

// Creates the initial snake head node
let createSnakeHead = (boardSize) =>{
    const randomNumber = Math.floor(Math.random() * boardSize)
    let snakeHead = document.getElementById(randomNumber)
    snakeHead.classList.add('snakeHead')
    return String(randomNumber)
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

    // creating random rgb values
    // let r = String(Math.floor(Math.random() * 255))
    // let g = String(Math.floor(Math.random() * 255))
    // let b = String(Math.floor(Math.random() * 255))
    // console.log(r,g,b)

    // assign random background
    // oldHead.style.backgroundColor=`rgb(${r},${g},${b})`;

    // set the how long it will last using the 'level' setting as a timer starting number
    oldHead.setAttribute('value', level)
    
    // Array containing all existing body sections of the snake
    let snakeBody = document.getElementsByClassName('snakeBody')

    // for every section of the body
    for(let i=0;i<=snakeBody.length;i++){
        // save section to variable
        let section = snakeBody.item(i)
        // get the value of it's existing timer
        let timer = parseInt(section.getAttribute('value'))

        // if the timer reaches zero
        if(timer < 1){
            // remove the counter from the sections html element
            section.removeAttribute('value')
            // remove the body from the html element
            section.classList.remove('snakeBody')
            // section.style.backgroundColor = 'gray'
        }
        // if there is still time on the timer
        else{
            // lower the timer by 1
            timer--
            // and update the section with the new timer value
            section.setAttribute('value', timer)
        }
    }
    return
}

let createScoreboard =()=>{
    // get board html element
    let board = document.getElementById('scoreboard')
    // add style for scoreboard
    board.classList.add('scoreboard')
    board.style.display = 'flex'
    board.style.justifyContent = 'center'
    // create score counter element
    let scoreCounter = document.createElement('h1')
    // set counter to current level
    scoreCounter.innerText = `Score: ${level}`
    scoreCounter.id = 'currentScore'
    // add it to the DOM
    board.appendChild(scoreCounter)
}
let updateScoreboard =()=>{
    let currentScore = document.getElementById('currentScore')
    currentScore.innerText = `Score: ${level}`
}

// Run setup functions
createBoard(boardSize)
createGoal(boardSize)
createSnakeHead(boardSize)
createScoreboard()



// -----[ Game Runtime ]-----
let runtime=()=>{

    // -- Movement Listener --
    $(document).keydown(function(event){
        // goal location
        let goal = document.getElementsByClassName('goalSquare')[0]
        let goalLocation = goal.id

        // location of snake head
        let oldHead = document.getElementsByClassName('snakeHead')[0]
        // ID from it's division
        let location = parseInt(oldHead.id)
        // initializing new location
        let newLocation = '0'
        

        // [ KEY PRESSES ]
        switch (event.which){
            case 37: // LEFT
                // find new location
                    newLocation = String(parseInt(oldHead.id) - 1)
                // grab division id of new location
                newHead = document.getElementById(newLocation)
                // check if the new location is within the boundries
                if(parseInt(location) % width === 0){
                    // if new location is out of bounds, do nothing
                    return
                }
                break;


            case 38: // UP
                newLocation = String(parseInt(oldHead.id) - width)
                newHead = document.getElementById(newLocation)
                if(parseInt(newLocation) < 0){
                    return
                }
                break;      

                
            case 39: // RIGHT
                newLocation = String(parseInt(oldHead.id) + 1)
                newHead = document.getElementById(newLocation)
                if(parseInt(newLocation) % width === 0){
                    return
                }
                break;


            case 40: // DOWN
                newLocation = String(parseInt(oldHead.id) + width)
                newHead = document.getElementById(newLocation)
                if(parseInt(newLocation) > boardSize-1){
                    return
                }
                break;
        }

        // move the snake
        moveSnake(oldHead,newHead)
        // Checking if snake reached the goal
        if (newLocation === goalLocation){
            // remove the goal
            goal.classList.remove('goalSquare')
            // place a new one
            createGoal(boardSize)
            // enlarge snake by 1
            growSnake()

            console.log('GOAL!!')
            updateScoreboard()

        }
    });
    

}


// Run Game
runtime()