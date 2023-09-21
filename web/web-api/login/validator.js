var form =document.forms['dados']
var btn_submit=document.getElementById('btn-send')

btn_submit.addEventListener('click',function(event){
    alert('ok')
    for (var i in form.elements){
        console.log(i)
    }
})