const cv_width=350
const cv_height =350

const canvas=document.querySelector("#canvas")
      canvas.width=cv_width
      canvas.height=cv_height
 
const ctx=canvas.getContext('2d')

class Circunferencia{
    x;y;radius;
    constructor( radius){
        this.x=cv_width/2;
        this.y=cv_height/2;
        this.radius=radius;
        this.draw_arc(ctx)
        this.draw_x_axis(ctx)
        this.draw_y_axis(ctx)
        this.desenhar_cateto_oposto(ctx)
        this.desenhar_cateto_adjacente(ctx)


    }
    draw_arc(ctx){
        ctx.beginPath()
        ctx.strokeStyle='blue'
        ctx.arc(this.x,this.y,this.radius,0,Math.PI*2)
        ctx.stroke()
        ctx.closePath()
    }

    draw_x_axis(ctx){
        ctx.beginPath()
        ctx.strokeStyle='red'
        ctx.moveTo(0,this.y)
        ctx.lineTo(cv_width,this.y)
        ctx.stroke()
        ctx.closePath()
    }
    draw_y_axis(ctx){
        ctx.beginPath()
        ctx.strokeStyle='rgb(9, 255, 91)'
        ctx.moveTo(this.x,0)
        ctx.lineTo(this.x,cv_height)
        ctx.stroke()
        ctx.closePath()
    }

    desenhar_cateto_oposto(ctx){
        ctx.beginPath()
        ctx.strokeStyle='green'
        ctx.moveTo(this.x+5,this.y-5)
        ctx.lineTo(this.x+this.radius,this.y-5)
        ctx.strokeStyle='rgb(25, 0, 12)'
        ctx.stroke()
        ctx.closePath()
        
    }
    desenhar_cateto_adjacente(ctx){
        ctx.beginPath()
        ctx.strokeStyle='rgb(25, 0, 12)'
        ctx.moveTo(this.x+5,this.y-5)
        ctx.lineTo(this.x+90,this.y+this.radius*-1)
        ctx.stroke()
        ctx.closePath()
    }
    
}
const circunf = new Circunferencia( 150)
// circunf.draw_arc(ctx)
// circunf.draw_x_axis(ctx)

