var btn=document.getElementsByClassName('button')
btn.innerHTML='+'
var cv =document.getElementById('canvas');
const cv_wid=450;
const cv_heig=400;
var x =20;
var y=10;
var resx=document.getElementById('xres')
var resy=document.getElementById('yres')

var ctx=cv.getContext('2d')
drawcircle()

function drawcircle(){
    cv.width=400
    cv.height=400
    ctx.beginPath()
    ctx.arc(cv.width/2, cv.height/2, 180, 0, 2*Math.PI);
    ctx.strokeStyle='#117437'
    ctx.stroke()
  
    updare_res()
}

function draw_dot(){
    ctx.beginPath()
    
    ctx.arc(cv.width-x,cv.height/2-y,10,0,2*Math.PI)
    ctx.fillStyle='#E6DFE4';
    ctx.fill()
    updare_res()
}

function decrement(){
    x+=1;
    y+=1;
    updare_res()
}
function increment(){
    x-=1;
    y-=1;
    updare_res()
}
function updare_res(){
    resx.innerHTML=x;
    resy.innerHTML=y;
    draw_dot()
    drawcircle()
}
function draw_axis(){
    
}