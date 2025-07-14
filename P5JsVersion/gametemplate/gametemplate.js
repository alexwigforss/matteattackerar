let bg;
let started = false;
let w,h;

function preload() {
  bg = loadImage('assets/bild.jpg');
}

function setup() {
  w = 720;
  h = 400;
  createCanvas(w, h);
  initStartScreen();
}

function draw() {
  if(!started){
  startscreen();
  } else if (started){
    levels();
  }
}
