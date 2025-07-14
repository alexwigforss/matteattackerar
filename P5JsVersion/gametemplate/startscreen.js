let scrollWidth;

function initStartScreen() {
  scrollWidth = width + 200;
  textSize(32);
  textAlign(RIGHT, CENTER);
  button = createButton('S T A R T');
  button.position(width/2, height);
  button.mousePressed(startGame);
}

function startscreen() {
  background(bg);
  fill(0, 102, 153);
  text('spelets namn', scrollWidth-(frameCount * 2) % scrollWidth, 60);
}

function startGame() {
  started = true;
  button.hide();
  initLevels();
}
