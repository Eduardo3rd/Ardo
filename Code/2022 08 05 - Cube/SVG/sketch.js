function setup() {
  //set the canvas size in pixels 
  createCanvas(1000, 1000, SVG);
  //set the background color to black 
  background(255);
  //only draw the piece one time 
  noLoop();
}

function cube(x,y,size) {
  //draw a box 
  square(x,y,size);
  
  corners = [];
  corn = [];
  
  corners.push([x,y])
  corners.push([x+size,y])
  corners.push([x+size,y+size])
  corners.push([x,y+size])
  
  corn.push([x+size/2,y+size/2])
  corn.push([x+3*size/2,y+size/2])
  corn.push([x+3*size/2,y+3*size/2])
  corn.push([x+size/2,y+3*size/2])
  
  line(corners[0][0],corners[0][1],corn[0][0],corn[0][1]);
  line(corners[1][0],corners[1][1],corn[1][0],corn[1][1]);
  line(corners[2][0],corners[2][1],corn[2][0],corn[2][1]);
  line(corners[3][0],corners[3][1],corn[3][0],corn[3][1]);
  
  square(corn[0][0],corn[0][1],size)
  
}

function draw() {  
  //set the stroke color to white 
  stroke(0);
  //set the stroke width to 1 pixel 
  strokeWeight(1);
  //make all shapes outlines only 
  noFill(); 
  
  step = 1
  for (var i = 0; i <= 6; i += step) {
    cube(random(0,500),random(0,500),random(10,200))
  }
  
  //cube(100,100,500)
  //cube(50,50,50)
  //cube()
  
  
  
  

//save("output.svg");
  
  
}


