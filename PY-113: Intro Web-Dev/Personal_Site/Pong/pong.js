let canvas = document.getElementById('canvas')
let context = canvas.getContext('2d')

// initial ball location and direction
canvas.width = 1000
canvas.height = canvas.width*.8
let ballX = canvas.width/2;
let ballY = canvas.height/2;
let ballSpeed = 1.0
let directionX = 1 * ballSpeed;
let directionY = 1 * ballSpeed;
let ballSize = 5
let ballHits = 0
let paddle1X = canvas.width - 14
let paddle1Y = canvas.height/2
let paddle1Width = 10
let paddle1Height = 100
let paddle1Speed = 1.5
let up1,down1,left1,right1 = false
let paddleHit1 = false

let paddle2X = 4
let paddle2Y = canvas.height/2
let paddle2Width = 10
let paddle2Height = 100
let paddle2Speed = 1.7
let up2,down2,left2,right2 = false
let paddleHit2 = false

let impactPosition = 0

let twoPlayer = false
let noPlayer = false

let aiSpeed1 = 2
let aiSpeed2 = 2


// construct player 1 paddle
let drawPaddle1=()=>{
    context.beginPath();
    context.rect(paddle1X, paddle1Y, paddle1Width, paddle1Height);
    context.fillStyle = "#0095DD";
    context.fill();
    context.closePath();
}

// construct player 2 paddle
let drawPaddle2=()=>{
    context.beginPath();
    context.rect(paddle2X, paddle2Y, paddle2Width, paddle2Height);
    context.fillStyle = "#0095DD";
    context.fill();
    context.closePath();
}

// construct ball
let drawBall=()=>{
    context.beginPath();
    context.arc(ballX, ballY, ballSize, 0, Math.PI*2);
    context.fillStyle = "#0095DD";
    context.fill();
    context.closePath();
}

// clear canvas on every frame
let clearCanvas=()=>{
    // clear the canvas of previous frames items
    context.clearRect(0, 0, canvas.width, canvas.height);
}

// move ball to next location
let moveBall=()=>{
    // adjust balls location coordinates with direction vector
    ballX += directionX * ballSpeed;
    ballY += directionY * ballSpeed;
}
// adjust speed of ball
let updateBallSpeed=()=>{
    if(ballHits >= 3){
        ballSpeed += .15
        ballHits = 0
        console.log('ball speed increased :', ballSpeed)
    }
    else{

    }
}
// move paddle the user has pressed keys
let movePaddle1=()=>{
    if(up1){
        paddle1Y -= paddle1Speed;
    }
    else if(down1){
        paddle1Y += paddle1Speed;
    }
    else if(up2){
        paddle2Y -= paddle2Speed;
    }
    else if(down2){
        paddle2Y += paddle2Speed;
    }
}
let movePaddle2=()=>{
    if(up2){
        paddle2Y -= paddle2Speed;
    }
    else if(down2){
        paddle2Y += paddle2Speed;
    }
    else if(up2){
        paddle2Y -= paddle2Speed;
    }
    else if(down2){
        paddle2Y += paddle2Speed;
    }
}
let ai1=()=>{
    // if ball is on ai's third of the court
    if(ballX < canvas.width/2 & directionX < 0){
        // if ball is over ai, move up
        if(paddle2Y+paddle2Height/2 > ballY+ballSize/2){
            paddle2Y -= aiSpeed1
        }
        // otherwise move lower
        else if(paddle2Y+paddle2Height/2 < ballY+ballSize/2){
            paddle2Y += aiSpeed1
        }
    }
    // if ball on opponents side, move paddle to center of y axis
    else{
        if(paddle2Y+paddle2Height/2 > canvas.height/2){
            paddle2Y-=aiSpeed1
        }
        else{
            paddle2Y+=aiSpeed1
        }
    }
}
let ai2=()=>{
    // if ball is on ai's third of the court
    if(ballX > canvas.width - canvas.width/4 & directionX > 0){
        // if ball is over ai, move up
        if(paddle1Y+paddle1Height/2 > ballY+ballSize/2){
            paddle1Y -= aiSpeed2
        }
        // otherwise move lower
        else if(paddle1Y+paddle1Height/2 < ballY+ballSize/2){
            paddle1Y += aiSpeed2
        }
    }
    // if ball on opponents side, move paddle to center of y axis
    else{
        if(paddle1Y+paddle1Height/2 > canvas.height/2){
            paddle1Y-= aiSpeed2
        }
        else{
            paddle1Y+= aiSpeed2
        }
    }
}

// check for ball impact with wall
let wallCollision=()=>{
    // next ball Y position is off the canvas edge
    if(ballY + directionY*ballSpeed - ballSize < 0 || ballY + directionY*ballSpeed + ballSize > canvas.height) {
        // Flip the direction
        directionY = -directionY;
    }
    // if next ball X position is off left side
    if(ballX + directionX*ballSpeed - ballSize < 0) {
        // Flip the direction
        directionX = Math.abs(directionX);
        directionY = 0
        ballSpeed = 1
        console.log('Right Scored!')
    }
    else if(ballX + directionX*ballSpeed + ballSize >= canvas.width) {
        // Flip the direction
        directionX = Math.abs(directionX) * -1;
        directionY = 0
        ballSpeed = 1
        console.log('Left Scored!')

    }
}
let paddle1Collision=()=>{
    let [xCollision,yCollision] = [false,false]
    // player 1 paddle collision
    //  if ball is to the right (behind) paddle
    if(ballX + ballSize >= paddle1X){
        xCollision = true
    }
    //  y axis collision
    if(ballY + ballSize >= paddle1Y & ballY <= paddle1Y + paddle1Height){
        yCollision = true
    }
    // if ball hit paddle
    if(xCollision & yCollision){
        // determine what surface of paddle was hit
        // left (front) edge hit
        if(ballX <= paddle1X){    impactPosition = Math.abs((ballY + ballY * 1/2)-(paddle1Y+paddle1Height*1/2))
            directionX = Math.abs(directionX)*-1;
            ballX += directionX * ballSpeed
        }
        // top edge hit
        else if(ballY < paddle1Y + paddle1Height/2){
            directionY = Math.abs(directionY)*-1
            ballY += directionY * ballSpeed
        }
        // bottom edge hit
        else if(ballY > paddle1Y + paddle1Height/2){
            directionY = Math.abs(directionY)
            ballY += directionY * ballSpeed
        }
        paddleHit1 = true
        paddleHit2 = false
        ballHits++
        impactPosition = ( (ballY + ballSize * 1/2)- (paddle1Y+paddle1Height*1/2) ) / (paddle1Height/2)
        return true
    }
    return false
}

let paddle2Collision=()=>{
    let [xCollision,yCollision] = [false,false]
    // player 2 paddle collision
    //  if ball is to the left (behind) paddle
    if(ballX <= paddle2X + paddle2Width){
        xCollision = true
    }
    //  y axis collision
    if(ballY + ballSize >= paddle2Y & ballY <= paddle2Y + paddle2Height){
        yCollision = true
    }
    // if ball hit paddle
    if(xCollision & yCollision){
        // determine what surface of paddle was hit
        // right (front) edge hit
        if(ballX + ballSize > paddle2X + paddle2Width){
            directionX = Math.abs(directionX);
            ballX += directionX * ballSpeed
        }
        // top edge hit
        else if(ballY < paddle2Y + paddle2Height/2){
            directionY = Math.abs(directionY)*-1
            ballY += directionY * ballSpeed
        }
        // bottom edge hit
        else if(ballY > paddle2Y + paddle2Height/2){
            directionY = Math.abs(directionY)
            ballY += directionY * ballSpeed
        }
        paddleHit2 = true
        paddleHit1 = false
        ballHits++
        // console.log((ballY + ballSize * 1/2)  ,(paddle2Y+paddle2Height*1/2), (ballY + ballSize * 1/2)-(paddle2Y+paddle2Height*1/2), (paddle2Height/2))
        impactPosition = ((ballY + ballSize * 1/2)-(paddle2Y+paddle2Height*1/2))/(paddle2Height/2)
        return true
    }
    return false
}

let updateBallAngle=()=>{
    if(impactPosition){
        console.log(impactPosition)
        directionY = 5 * impactPosition
        if(directionY>1.5){
            directionY=1.5
        }
    }
    impactPosition = false
}

// game loop
let draw=()=>{
    clearCanvas();
    moveBall()
    updateBallSpeed()
    drawBall();
    if(noPlayer){
        ai2()
    }
    else{
        movePaddle1()
    }
    if(twoPlayer){
        movePaddle2()
    }
    else{
        ai1()
    }
    drawPaddle1()
    drawPaddle2();
    wallCollision();
    paddle1Collision()
    paddle2Collision()
    updateBallAngle()

}
setInterval(draw, 1);


// move paddle
$(document).keydown((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 37: // LEFT
            left1 = true
            break;

        case 38: // UP
            up1 = true
            break;      
          
        case 39: // RIGHT
            right1 = true
            break;

        case 40: // DOWN
            down1 = true
            break;
    }
});
$(document).keydown((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 65: // A
            left2 = true
            break;

        case 87: // W
            up2 = true
            break;      
          
        case 68: // D
            right2 = true
            break;

        case 83: // S
            down2 = true
            break;
    }
});
// stop paddle
$(document).keyup((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 37: // LEFT
            left1 = false
            break;

        case 38: // UP
            up1 = false
            break;      
          
        case 39: // RIGHT
            right1 = false
            break;

        case 40: // DOWN
            down1 = false
            break;
    }
});
$(document).keyup((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 65: // A
            left2 = false
            break;

        case 87: // W
            up2 = false
            break;      
          
        case 68: // D
            right2 = false
            break;

        case 83: // S
            down2 = false
            break;
    }
});


// Prevent arrows scrolling the page
window.addEventListener("keydown", function(e) {
    if(["Space","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {
        e.preventDefault();
    }
}, false);
