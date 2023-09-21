let root=document.documentElement;
let primarRedVar=document.getElementById('pulse-red')
let primarBlueVar=document.getElementById('pulse-blue')

const colorPrimary =getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim()
const colorPrimaryBlue =getComputedStyle(document.documentElement).getPropertyValue('--primary-color-blue').trim()
const colorPrimaryRed =getComputedStyle(document.documentElement).getPropertyValue('--primary-color-red').trim()
const colorLabel =getComputedStyle(document.documentElement).getPropertyValue('--color-label').trim()
const fontFamily =getComputedStyle(document.documentElement).getPropertyValue('--font-family').trim()

 
root.addEventListener('click',e=>{
    root.style.setProperty('--primary-color','red')
})
primarRedVar.addEventListener('click',e=>{
    root.style.setProperty('--primary-color',colorPrimaryRed)
})
primarBlueVar.addEventListener('click',e=>{
    root.style.setProperty('--primary-color',colorPrimaryBlue)
})

const canvas =document.getElementById('canvas')
const ctx =canvas.getContext('2d')
const width=800
const graphic_width=780;
const height=200
const graphic_height=180;
canvas.setAttribute('width',width)
canvas.setAttribute('height',height)
 
draw_YaxisVerticalLinesWithlegends()
draw_xAxsisHorizontalLines()
plotDataIntoGraph()
// plotDataIntoGraphCirc()
function draw_YaxisVerticalLinesWithlegends(){
    const dias =['Dom','Seg','Ter','Qua','Qui','Sex','Sab']
    const nr_of_lines=7;
    const X_divider=graphic_width/nr_of_lines;
    var start_ypoint=20;
    var start_xPoint=20;
    ctx.beginPath()
    
    ctx.strokeStyle=colorLabel;
    ctx.fillStyle = 'white';
    for(var i=0;i<nr_of_lines;i++){
        ctx.lineWidth=0.2

        ctx.moveTo(start_xPoint,graphic_height)
        ctx.lineTo(start_xPoint,0)
        ctx.stroke()
       
        
        ctx.fillStyle='white'
        ctx.font = 'bold 12px Arial';
        ctx.fillText(dias[i],start_xPoint-6,graphic_height+20)
        //dias de semana
    start_xPoint+=X_divider
     
    }
    ctx.closePath()
    ctx.beginPath()
    ctx.moveTo(10,graphic_height)
    ctx.lineTo(width,graphic_height)
    ctx.stroke()
}

function draw_xAxsisHorizontalLines(){
    const total_transByday =[0,1,2,3,4,5,6,7,8,9,10]
    const nr_of_lines=total_transByday.length;
    const y_divider=graphic_height/nr_of_lines;
    var start_ypoint=20;
    var start_xPoint=20;
    ctx.beginPath()
    for(var i=1;i<nr_of_lines;i++){
        ctx.strokeStyle=colorPrimary
        ctx.moveTo(start_xPoint-10,start_ypoint)
        ctx.lineTo(graphic_width,start_ypoint)
        ctx.lineWidth=0.2
        ctx.stroke()

        //legendas
        ctx.fillStyle='white'
        ctx.font = 'bold 12px Arial';
        ctx.fillText(total_transByday[nr_of_lines-i],0,start_ypoint+5)

        start_ypoint+=y_divider
    }
    ctx.closePath()
}
plotDataIntoGraph()

function plotDataIntoGraph(){
    var dados=[2,8,4,6,10,3,7,8]
    start_xPoint=20;
    const X_divider=graphic_width/dados.length;
    ctx.beginPath()
    ctx.strokeStyle=colorPrimary
      var start_ypoint=20;
    dados.forEach((dado)=>{
        ctx.lineWidth=1
        // ctx.moveTo(start_xPoint,20)
        ctx.lineTo(start_xPoint, graphic_height-((start_ypoint-5)*dado))
        ctx.stroke()
        start_xPoint+=X_divider
    })
    ctx.closePath()
}
var _valores=[7,6,4,10,8,2,4]
var rand=Math.random()*10;
function update(){

    _valores=[Math.random()*10,Math.random()*10,Math.random()*10,rand,Math.random()*10,Math.random()*10,Math.random()*10,Math.random()*10]

}
// setInterval(update,1000)
plotDataIntoGraphCirc(_valores)

function plotDataIntoGraphCirc(_valores){
    
    start_xPoint=20;
    const X_divider=graphic_width/_valores.length;
    ctx.beginPath()
    ctx.strokeStyle='red'
      var start_ypoint=20;
    _valores.forEach((dado)=>{
        ctx.lineWidth=2
        // ctx.moveTo(start_xPoint,20)
        ctx.lineJoin='round'
        ctx.lineTo(start_xPoint, graphic_height-((start_ypoint-5)*dado))
        ctx.stroke()
        start_xPoint+=X_divider+10

        // ctx.closePath()
        // ctx.arc(start_xPoint, graphic_height-((start_ypoint-5)*dado),10,0,Math.PI*2)
        // ctx.stroke()
    })
    // ctx.closePath()
    GraphCirc(_valores)
}
function  GraphCirc(_valores){
    
    start_xPoint=20;
    const X_divider=graphic_width/_valores.length;
    ctx.strokeStyle='red'
    var start_ypoint=20;
    _valores.forEach((dado)=>{
        ctx.beginPath()
        ctx.lineWidth=2
        ctx.arc(start_xPoint, graphic_height-((start_ypoint-5)*dado),10,0,Math.PI*2)
        ctx.fill()
        start_xPoint+=X_divider+10
        ctx.closePath()
    })
}