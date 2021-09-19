function setup() {
  createCanvas(1000, 1000);
  background(360);
  noLoop();
}

function draw() {
  for (var x = 0; x <= width; x += width / 100) {
    for (var y = 0; y <= height; y += height / 100) {
      stroke(0);
      strokeWeight(1);
      line(x, 0, x, height);
      line(0, y, width, y);
    }
  }
  //arc(x, y, w, h, start, stop, [mode], [detail])
  
  t = random(0,1)
  b = random(0,1)
  r = random(0,1)
  l = random(0,1)
  
  print(t)
  


  for (var circ = 0; circ <= 2; circ += .01){
    if (t > 0.5){
      arc(width/2, 0, width*circ, height*circ, 0, 2*PI);
    }
    
    if (r > 0.5){
      arc(width, height/2, width*circ, height*circ, 0, 2*PI);
    }
    
    if (l > 0.5){
      arc(0, height/2, width*circ, height*circ, 0, 2*PI);
    }
    
    if (b > 0.5){
      arc(width/2, height, width*circ, height*circ, 0, 2*PI);
    }
    noFill(); 
  }
  
}
