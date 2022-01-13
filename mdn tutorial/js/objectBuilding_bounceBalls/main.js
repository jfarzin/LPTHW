// setup canvas

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;

const para = document.querySelector('p');
let initialBallCount = 0;
let ballCount = 25;
let captured = [0,0];

// function to generate random number

function random(min, max) {
  const num = Math.floor(Math.random() * (max - min + 1)) + min;
  return num;
}


function Shape(x, y, velX, velY, exists) {
  this.x = x;
  this.y = y;
  this.velX = velX;
  this.velY = velY;
  this.exists = exists;
}

function Ball(x, y, velX, velY, exists, color, size) {
  Shape.call(this, x, y, velX, velY, exists);
  
  this.color = color;
  this.size = size;
}

Ball.prototype = Object.create(Shape.prototype);
Object.defineProperty(Ball.prototype, 'constructor', {
    value: Ball,
    enumerable: false,
    writable: true 
  });
  

Ball.prototype.draw = function() {
  ctx.beginPath();
  ctx.fillStyle = this.color;
  ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
  ctx.fill();
}

Ball.prototype.update = function() {
  if ((this.x + this.size) >= width) {
    this.velX = -(this.velX);
  }
  if ((this.x - this.size) <= 0) {
    this.velX = -(this.velX);
  }
  if ((this.y - this.size) <= 0) {
    this.velY = -(this.velY);
  }
  if ((this.y + this.size) >= height) {
    this.velY = -(this.velY);
  }

  this.x += this.velX;
  this.y += this.velY;
}

Ball.prototype.collisionDetect = function() {
  for (let j = 0; j < balls.length; j++) {
    if (!(this === balls[j]) && balls[j].exists) {
      const dx = this.x - balls[j].x;
      const dy = this.y - balls[j].y;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < this.size + balls[j].size) {
        balls[j].color = this.color = 'rgb(' + random(0,255) + ',' + random(0,255) + ',' + random(0,255) + ')';
      }
    }
  }
}

function EvilCircle(x, y, velX, velY, exists, color, size, captured) {
  Shape.call(this, x, y, velX, velY, exists);

  this.velX = 20; 
  this.velY = 20;
  this.color = color;
  this.size = size;
  this.captured = captured;
}

EvilCircle.prototype = Object.create(Shape.prototype);
Object.defineProperty(EvilCircle.prototype, 'constructor', {
    value: EvilCircle,
    enumerable: false,
    writable: true 
  });

  EvilCircle.prototype.draw = function() {
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = this.color;
    ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
    ctx.stroke();
  }
  
  EvilCircle.prototype.checkBounds = function() {
    if ((this.x + this.size) >= width) {
      this.x -= this.size;
    }
    if ((this.x - this.size) <= 0) {
      this.x += this.size;
    }
    if ((this.y - this.size) <= 0) {
      this.y += this.size;
    }
    if ((this.y + this.size) >= height) {
      this.y -= this.size;
    }
  }
  
  EvilCircle.prototype.setControls = function() {
    let _this = this;
    window.onkeydown = function(e) {
      if (e.key === 'a') {
        _this.x -= _this.velX;
      } else if (e.key === 'd') {
        _this.x += _this.velX;
      } else if (e.key === 'w') {
        _this.y -= _this.velY;
      } else if (e.key ==='s') {
        _this.y += _this.velY;
      }


      if (e.key === 'j') {
        _this.x -= _this.velX;
      } else if (e.key === 'l') {
        _this.x += _this.velX;
      } else if (e.key === 'i') {
        _this.y -= _this.velY;
      } else if (e.key ==='k') {
        _this.y += _this.velY;
      }

    }
  }
  
  /*
  EvilCircle.prototype.setControls2 = function() {
    let _this = this;
    window.onkeydown = function(e) {
      if (e.keyCode === '37') {
         // left
        _this.x -= _this.velX;
      } else if (e.keyCode === '39') {
        // right
        _this.x += _this.velX;
      } else if (e.keyCode === '38') {
        // up
        _this.y -= _this.velY;
      } else if (e.keyCode === '40') {
        //down
        _this.y += _this.velY;
      }
    }
  }
 */

  EvilCircle.prototype.collisionDetect = function() {
    for (let j = 0; j < balls.length; j++) {
      if (balls[j].exists) {
        const dx = this.x - balls[j].x;
        const dy = this.y - balls[j].y;
        const distance = Math.sqrt(dx * dx + dy * dy);
  
        if (distance < this.size + balls[j].size) {
          balls[j].exists = this.exists = false;
          initialBallCount = ballCount;
          ballCount -= 1;
        }
      }
    }
  }
  

let balls = [];

while (balls.length < 25) {
  let size = random(10,20);
  let ball = new Ball(
    // ball position always drawn at least one ball width
    // away from the edge of the canvas, to avoid drawing errors
    random(0 + size, width - size),
    random(0 + size, height - size),
    random(-7,7),
    random(-7,7),
    true,
    'rgb(' + random(0,255) + ',' + random(0,255) + ',' + random(0,255) + ')',
    size
  );
  balls.push(ball); 
};

/*
let players = [];

while (players.length < 2) {
  let ecsize = random(10,20);
  let evilCircle = new EvilCircle(
    random(0 + ecsize, width - ecsize),
    random(0 + ecsize, height - ecsize),
    20,
    20,
    true,
    'white',
    ecsize,
    0  
  );
  players.push(evilCircle);  
};

players[0].setControls1;
players[1].setControls2;
*/

let ecsize = 14;
let evilCircle1 = new EvilCircle(
  random(0 + ecsize, width - ecsize),
  random(0 + ecsize, height - ecsize),
  20,
  20,
  true,
  'white', 
  14,
  0
);
evilCircle1.setControls();

let evilCircle2 = new EvilCircle(
  random(0 + ecsize, width - ecsize),
  random(0 + ecsize, height - ecsize),
  20,
  20,
  true,
  'yellow',
  14,
  0
);
evilCircle2.setControls();

let players = [evilCircle1, evilCircle2];


function loop() {
  ctx.fillStyle = 'rgba(0,0,0,0.25)';
  ctx.fillRect(0, 0, width, height);

  for (let i = 0; i < balls.length; i++) {
    if (balls[i].exists === true) {
      balls[i].draw();
      balls[i].update();
      balls[i].collisionDetect();
      
      evilCircle1.draw();
      evilCircle1.checkBounds();
      evilCircle1.collisionDetect();

      evilCircle2.draw();
      evilCircle2.checkBounds();
      evilCircle2.collisionDetect();
      
      /*
      for (let p = 0; p < players.length; p++) {
        players[p].draw();
        players[p].checkBounds();
        players[p].collisionDetect();
      }
      */
    }
  }

  para.textContent = 'Ball count: ' + ballCount + ' || Player1: ' + captured[0] + '; Player2: ' + captured[1];

  requestAnimationFrame(loop);
}

loop();