let container =document.getElementById('container')

// getting the root of vars of css
let _root=document.documentElement;

//geting dots with colors red and blue
let _primarRedVar=document.getElementById('pulse-red')
let _primarBlueVar=document.getElementById('pulse-blue')


//Getting colors from css vars
const _colorPrimary =getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim()
const _colorPrimaryBlue =getComputedStyle(document.documentElement).getPropertyValue('--primary-color-blue').trim()
const _colorPrimaryRed =getComputedStyle(document.documentElement).getPropertyValue('--primary-color-red').trim()
const _colorLabel =getComputedStyle(document.documentElement).getPropertyValue('--color-label').trim()
const _fontFamily =getComputedStyle(document.documentElement).getPropertyValue('--font-family').trim()

// root.addEventListener(('click', e=>{
//     root.style.setProperty('--primary-color','red')
// }))
_primarBlueVar.addEventListener('click',e=>{
    _root.style.setProperty('--primary-color',_colorPrimaryBlue)
})
_primarRedVar.addEventListener('click',e=>{
    _root.style.setProperty('--primary-color',_colorPrimaryRed)
})

var math_canvas=document.getElementById('math-canvas')
    math_canvas.width=400
    math_canvas.height=400
    math_canvas.style.border=`1px solid ${_colorPrimaryRed}`
var _ctx=math_canvas.getContext('2d')

var x=math_canvas.width/2;
var y= math_canvas.height/2
var raio=150
function _draw_circunferency(){
    
    _ctx.clearRect(0,0,400,400)
    _ctx.beginPath()
    _ctx.arc(x,y,raio,0,2*Math.PI)
    _ctx.fillStyle=_colorPrimaryRed
    _ctx.stroke()
    _ctx.closePath()
}
function draw_ycoords(){
    _ctx.beginPath()
    _ctx.moveTo(x,0)
    _ctx.strokeStyle='white'
    _ctx.lineTo(x,400)
    _ctx.stroke()
    
}
_draw_circunferency()
draw_ycoords()

function draw_xcoords(){
    _ctx.beginPath()
    _ctx.moveTo(0,y)
    _ctx.strokeStyle='RED'
    _ctx.lineTo(400,y)
    _ctx.stroke()
}
draw_xcoords()

function _draw_tringle(){
    var posx=60;
    var posy=100;
    var xraio=raio;

    _ctx.beginPath()
    _ctx.moveTo( x, y)
    _ctx.lineTo( x+raio-posx, y)
    _ctx.strokeStyle='black'
    // _ctx.strokewidth=3
    _ctx.stroke()
}

 _draw_tringle()

