let canvas = document.getElementById('canvas')
let context = canvas.getContext('2d')

// initial player location and direction

canvas.style.cursor = "none";
let mouseX = 0
let mouseY = 0
let playerSpeed = 1.5
let directionX = 0;
let directionY = 0;
let playerSize = 10
let enemySize = 25
let bulletSize = 2

let [up,down,left,right] = [false,false,false,false]
let mouseClicked = false
let [mouseClickX,mouseClickY] = [false,false]

let players = []
let enemies = []
let bullets = []


let createPlayer=()=>{
    let player = new Player('player')
    players.push(player)
}
let createEnemy=()=>{
    let enemy = new Enemy('enemy')
    enemies.push(enemy)
}
let createBullet=()=>{
    let bullet = new Bullet('bullet')
    bullets.push(bullet)
}

// clear canvas on every frame
let clearCanvas=()=>{
    // clear the canvas of previous frames items
    context.clearRect(0, 0, canvas.width, canvas.height);
}

// game loop
let draw=()=>{
    // Clear all items every frame
    clearCanvas()
    // Allow player to spawn
    if(players.length < 1){
        createPlayer()
    }
    if(enemies.length === 0){
        createEnemy()
    }
    // Players
    players.forEach(player => player.move())
    // Enemies
    enemies.forEach(enemies => enemies.move())
    // Bullets
    bullets.forEach(bullet => bullet.move())
}
setInterval(draw, 16)



// construct player

class Player {
    constructor() {
      this.name = 'player'
      this.locationX = canvas.width/2;
      this.locationY = canvas.height/2;
      this.health = 3
    }
    move(){
        if(this.health < 1){
            let index = players.indexOf(this);
            if (index > -1) {
                players.splice(index, 1);
            }
        }
        context.beginPath();
        this.locationX += directionX * playerSpeed;
        this.locationY += directionY * playerSpeed;
        context.arc(this.locationX, this.locationY, playerSize, 0, Math.PI*2);
        context.fillStyle = "#FFFFFF";
        context.fill();
        context.closePath();
    }
}
class Enemy {
    constructor() {
        this.name = 'enemy'
        this.size = enemySize
        this.locationX = Math.floor(Math.random() * canvas.width);
        this.locationY = Math.floor(Math.random() * canvas.height);
        this.targetX = players[0].locationX;
        this.targetY = players[0].locationY;
        this.directionX = this.targetX - this.locationX;
        this.directionY = this.targetY - this.locationY;
        this.targetReached = false;
        this.speed = .2
    }
    move(){
        if(this.targetReached){
            let index = enemies.indexOf(this);
            if (index > -1) {
                enemies.splice(index, 1);
                players[0].health--
            }
        }

        this.targetX = players[0].locationX
        this.targetY = players[0].locationY
        this.directionX = this.targetX - this.locationX;
        this.directionY = this.targetY - this.locationY;

        // Normalize the direction
        var len = Math.sqrt(this.directionX * this.directionX + this.directionY * this.directionY);
        this.directionX /= len;
        this.directionY /= len;
        // calculate remaining distance
        var dx = this.targetX - this.locationX;
        var dy = this.targetY - this.locationY;
        var lenSquared = dx * dx + dy * dy;
        // distance to cover in this update
        var distToCover = 5 * this.speed;
        // Check if the remaining distance is smaller than the 
        // distance to cover. If yes, set location to target location.
        // Also set the "targetReached" flag to true
        if(lenSquared < distToCover * distToCover + this.size*65){
            // this.locationX = this.targetX;
            // this.locationY = this.targetY;
            this.targetReached = true;
        } else {
            this.locationX += distToCover * this.directionX;
            this.locationY += distToCover * this.directionY;
        }
        // draw the this on the screen
        context.beginPath();
        context.arc(this.locationX - bulletSize/2, this.locationY - bulletSize/2, this.size, 0, Math.PI*2);
        context.fillStyle = "#ff0000";
        context.fill()
        context.stroke();
    }
}
class Bullet {
    constructor() {
      this.name = 'name'
      this.locationX = players[0].locationX;
      this.locationY = players[0].locationY;
      this.targetX = mouseClickX;
      this.targetY = mouseClickY;
      this.directionX = this.targetX - this.locationX;
      this.directionY = this.targetY - this.locationY;
      this.targetReached = false;
    }

    move(){
        if(this.targetReached){
            let index = bullets.indexOf(this);
            if (index > -1) {
                bullets.splice(index, 1);
            }
        }
        enemies.forEach(target=>{
            // Normalize the direction
            var len = Math.sqrt(this.directionX * this.directionX + this.directionY * this.directionY);
            this.directionX /= len;
            this.directionY /= len;
            // calculate remaining distance
            var dx = target.locationX - this.locationX;
            var dy = target.locationY - this.locationY;
            var lenSquared = dx * dx + dy * dy;
            // distance to cover in this update
            var distToCover = 5 * 1;
            // Check if the remaining distance is smaller than the 
            // distance to cover. If yes, set location to target location.
            // Also set the "targetReached" flag to true
            if(lenSquared < distToCover * distToCover + 50*target.size){
                console.log('hit')
                let index = bullets.indexOf(this);
                if (index > -1) {
                    bullets.splice(index, 1);
                }
                index = enemies.indexOf(target);
                if (index > -1) {
                    enemies.splice(index, 1);
                }
            }
        })
        // Normalize the direction
        var len = Math.sqrt(this.directionX * this.directionX + this.directionY * this.directionY);
        this.directionX /= len;
        this.directionY /= len;
        // calculate remaining distance
        var dx = this.targetX - this.locationX;
        var dy = this.targetY - this.locationY;
        var lenSquared = dx * dx + dy * dy;
        // distance to cover in this update
        var distToCover = 5 * 1;
        // Check if the remaining distance is smaller than the 
        // distance to cover. If yes, set location to target location.
        // Also set the "targetReached" flag to true
        if(lenSquared < distToCover * distToCover){
            this.locationX = this.targetX;
            this.locationY = this.targetY;
            this.targetReached = true;
        } else {
            this.locationX += distToCover * this.directionX;
            this.locationY += distToCover * this.directionY;
        }
        // draw the this on the screen
        context.beginPath();
        context.arc(this.locationX - bulletSize/2, this.locationY - bulletSize/2, bulletSize, 0, Math.PI*2);
        context.fillStyle = "#FFFFFF";
        context.fill()
        context.stroke();
    }
}
// Prevent arrows scrolling the page
window.addEventListener("keydown", function(e) {
    if(["Space","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {
        e.preventDefault();
    }
}, false);


// Mouse position reader and crosshair placement
$(document).ready(function() {
    // Setup our variables
    var cH = $('#crosshair-h'),
        cV = $('#crosshair-v');
    
    $(this).on('mousemove touchmove', function(e) {
      mouseX = e.pageX - 1;
      mouseY = e.pageY - 1;
      cH.css('top', e.pageY);
      cH.css('left', e.pageX);
      cV.css('top', e.pageY);
      cV.css('left', e.pageX);
    });
    
    // Anchor Hover Effects
    $("a").hover(function() {
      $(".hair").stop().css({borderColor: "#fff"}, 800)},
       function() {
      $(".hair").stop().css({borderColor: "black"},800)
    });
  });

  //report the mouse position on click
canvas.addEventListener("click", function (evt) {
    var mousePos = getMousePos(canvas, evt);
    mouseClickX = mousePos.x + 1
    mouseClickY = mousePos.y
    mouseClicked = true
    createBullet()
}, false);

//Get Mouse Position
function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}



// move player
$(document).keydown((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 37: // LEFT
            left = true
            directionX = -1 
            break;

        case 38: // UP
            up = true
            directionY = -1 
            break;      
          
        case 39: // RIGHT
            right = true
            directionX = 1 
            break;

        case 40: // DOWN
            down = true
            directionY = 1 
            break;
    }
});
$(document).keydown((event)=>{
    // [ KEY PRESSES ]
    switch (event.which){
        case 65: // A
            left = true
            directionX = -1 
            break;

        case 87: // W
            up = true
            directionY = -1 
            break;      
          
        case 68: // D
            right = true
            directionX = 1
            break;

        case 83: // S
            down = true
            directionY = 1
            break;
    }
});
// stop player
$(document).keyup((event)=>{
    // [ KEY RELEASE ]
    switch (event.which){
        case 37: // LEFT
            left = false
            directionX = 0;
            break;

        case 38: // UP
            up = false
            directionY = 0;
            break;      
          
        case 39: // RIGHT
            directionX = 0;
            right = false
            break;

        case 40: // DOWN
            down = false
            directionY = 0;
            break;
    }
});
$(document).keyup((event)=>{
    // [ KEY RELEASE ]
    switch (event.which){
        case 65: // A
            left = false
            directionX = 0;
            break;

        case 87: // W
            up = false
            directionY = 0;
            break;      
          
        case 68: // D
            right = false
            directionX = 0;
            break;

        case 83: // S
            down = false
            directionY = 0;
            break;
    }
});
