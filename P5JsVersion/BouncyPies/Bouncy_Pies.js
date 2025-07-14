let numBalls = 5;
let spring = 0.05;
let gravity = 0.03;
let friction = -0.8;
let balls = [];
let boxWidth;
let boxHeight;
let hUnit;
var msg = "MSG";
var leftButtons = new Array(10);
var rightButtons = new Array(10);
var l_left = 0
var l_right = 0
var timerValue;
var startButton;
var limit;
var result;
var rqoute;
// https://github.com/processing/p5.js/wiki/Positioning-your-canvas
function setup() {
  limit = 200
  setInterval(timeIt, 1000);
  timerValue = 2;
  textAlign(CENTER,CENTER);
  createCanvas(600, 550);
  margin = 100;
  two_margin = margin * 2;
  boxWidth = width - 2 * margin;
  boxHeight = height;
  hUnit = height/10
  msg = l_left + " / " + rqoute + " / " + l_right
  for (let nm = 1; nm < 11; nm++) {
    button = createButton('l ' + nm.toString(),'L' + nm);
    button.position(0, height / 10 * (nm-1));
    button.mousePressed(() => {
      sideBarPressed(-nm)
    });
  }
  for (let nm = 1; nm < 11; nm++) {
    button = createButton('r ' + nm.toString(),'R' + nm);
    button.position(width-margin, height / 10 * (nm-1));
    button.mousePressed(() => {
      sideBarPressed(nm)
    });
  }
  button = createButton('LAUNCH',0);
  button.position(0, height);
  button.id('launch');
  button.mousePressed(() => {
    launchPressed(0)
  });
  function sideBarPressed(n) {
    if (n < 0) {
      l_left = abs(n)
    } else if (n > 0) {
      l_right = n
    }
    //result = Math.round(l_left / l_right * 100) / 100;
    result = l_left / l_right;
    //rqoute = Math.round(result * 8 * 100) / 100;
    rqoute = result * 8;
    //msg = l_left + " / " + l_right + "\n" + result;
    msg = l_left + " / " + rqoute + " / " + l_right

  }
  function launchPressed(n) {
    msg = "L a u n c h";
    console.log("L a u n c h");

    console.log(balls[balls.length-1])
    for (var i = balls.length - 1; i >= 0; --i) {
      if (balls[i].quote == rqoute) {
        balls.splice(i,1);
        numBalls--;
      }
  }    //balls.pop();
    //numBalls--;
    
    //console.log(balls)
  }

  textAlign(CENTER);
  textSize(50);
  for (let i = 0; i < numBalls; i++) {
    balls[i] = new Ball(
      random(width),
      random(height),
      random(30, 100),
      i,
      balls
    );
  }
  noStroke();
}

function mouseReleased() {
  if (whereOnCanvas(mouseX,mouseY) == 1){
  balls[numBalls++] = new Ball(
    mouseX,
    mouseY,
    random(30, 70),
    numBalls,
    balls
    );
  }
}
function timeIt() {
  if (timerValue > 0) {
    timerValue--;
  } else {
    timerValue = 2;
    //console.log(timerValue);
  }
}
function legend(){
  fill(0);
  ellipse(width/4, height/10, 100, 100,1);
  fill(255);
  arc(width/4, height/10, 100, 100, HALF_PI, HALF_PI + QUARTER_PI * rqoute, PIE);

}
function draw() {
  background(255);
  if (timerValue == 0 && numBalls < limit) {
    balls[numBalls++] = new Ball(
      width/2,
      height/4,
      random(30, 70),
      numBalls,
      balls
      );
      timerValue = 2;
    }
  fill(255, 204);
  if (mouseIsPressed === true) {
    fill(0, 175);
    } else {
      fill(0, 175);
    }
    rect(100,0,boxWidth,height);
    fill(255, 104);
    balls.forEach(ball => {
      ball.collide();
      ball.move();
      ball.display();
    });
  text(msg,width/2,height/10);
  //text(str(mouseX)+" "+str(mouseY),width/2,height/2);
  legend();
}

function whereOnCanvas(x,y) {
  if (x < margin) {
    return 0
  } else if ((x < width - margin) && (y < 550)) {
    return 1
  } else if (x > width - margin) {
    return 2
  }
}

class Ball {
  constructor(xin, yin, din, idin, oin) {
    this.quote = round(random(1,9))
    //this.answer = Math.round(this.quote/8 * 100) / 100;
    this.answer = this.quote/8;
    this.x = xin;
    this.y = yin;
    this.vx = 0;
    this.vy = 0;
    this.diameter = din;
    this.id = idin;
    this.others = oin;
  }
  collide() {
    for (let i = this.id + 1; i < numBalls; i++) {
      let dx = this.others[i].x - this.x;
      let dy = this.others[i].y - this.y;
      let distance = sqrt(dx * dx + dy * dy);
      let minDist = this.others[i].diameter / 2 + this.diameter / 2;
      if (distance < minDist) {
        let angle = atan2(dy, dx);
        let targetX = this.x + cos(angle) * minDist;
        let targetY = this.y + sin(angle) * minDist;
        let ax = (targetX - this.others[i].x) * spring;
        let ay = (targetY - this.others[i].y) * spring;
        this.vx -= ax;
        this.vy -= ay;
        this.others[i].vx += ax;
        this.others[i].vy += ay;
      }
    }
  }
  move() {
    this.vy += gravity;
    this.x += this.vx;
    this.y += this.vy;
    if (this.x + this.diameter / 2 > margin + boxWidth) {
      this.x = margin + boxWidth - this.diameter / 2;
      this.vx *= friction;
    } else if (this.x - this.diameter / 2 < margin) {
      this.x = this.diameter / 2 + margin;
      this.vx *= friction;
    }
    if (this.y + this.diameter / 2 > height) {
      this.y = height - this.diameter / 2;
      this.vy *= friction;
    } else if (this.y - this.diameter / 2 < 0) {
      this.y = this.diameter / 2;
      this.vy *= friction;
    }
  }
  display() {
    //text(this.quote, this.x, this.y);
    if (this.quote == rqoute) {
      fill(0,255,0,100);
    } else {
      fill(0,0,255,100);
    }
    ellipse(this.x, this.y, this.diameter, this.diameter,1);
    arc(this.x, this.y, this.diameter, this.diameter, HALF_PI, HALF_PI + QUARTER_PI * this.quote, PIE);
    fill(0);
    textSize(16);
    text(this.quote, this.x, this.y);
    //text(this.answer, this.x, this.y);
  }
}
