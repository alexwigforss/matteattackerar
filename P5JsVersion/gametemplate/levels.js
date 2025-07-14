function levels() {
  background(255);
  drawGrid();
  fill(255, 102, 153);
  text('spelet startat', scrollWidth-(frameCount * 2) % scrollWidth, 60);
}

function drawGrid() {
  
  for(var i=0; i<height; i+=height/5){
    line(0, i, width, i);
  }
  for(var j=0; j<width; j+=width/10){
    line(j, 0, j, height);
  }
  
}
