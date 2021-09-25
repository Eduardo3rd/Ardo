function setup() {
  //set the canvas size in pixels 
  createCanvas(1100, 850, SVG);
  //set the background color to white 
  background(255);
  //only draw the piece one time 
  noLoop();
}

function draw() {  
  //set the stroke color to black 
  stroke(0);
  //set the stroke width to 1 pixel 
  strokeWeight(1);
  //make all shapes outlines only 
  noFill(); 
  
  //set the constants for the sin wave plot: 
  //y = (ScaleFactor)*sin(x/(CanvasWidth/Period)*(180deg)*CanvasHeight)+(CanvasHeight + OffsetFromMiddle) 

  //draw in the middle of the canvas
  offset = height/2
  //set the number of periods in the sin wave 
  //period = random(1,5)
  period = 2
  //set the step size between circles 
  step = 1
  //set the scale factor for the sin wave 
  //Yscale = random()
  Yscale = 0.5


  //initial x and y values for drawing the first circle 
  startX = width/2
  startY = height/2
  
  //set the radius of the mega circle 
  //scalar = random(10,50); 
  scalar = 200

  //set the number of circles in the mega circle. smaller numbers mean more circles 
  increment = random(0.01,0.02)*2*PI
  //set the diameter of the circles in the mega circle 
  dia = random(200,500)
  
  //for loop to draw all of the circles in this mega circle 
  for (var angle = 0; angle <= (2*PI); angle += increment) {
    //set the x and y cords for the circle 
    var x = startX + scalar * cos(angle);
    var y = startY + scalar * sin(angle);
    //draw the circle 
    arc(x, y, dia, dia, 0, 2*PI);
    }

save("output.svg");
  
  
}


