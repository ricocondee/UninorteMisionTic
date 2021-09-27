
/* const cambio = document.querySelector('.btn');

cambio.addEventListener('click',function(){
document.body.classList.toggle('darktheme');

var tema = document.body.className;
    if(tema == 'lighttheme'){
        this.textContent = "Dark";
    }else{
        this.textContent = "Light";
    }
}); */


var checkbox = document.getElementById('toggle');

checkbox.addEventListener('change', function () {
    if (this.checked) {
        document.body.className = 'darktheme';
    }
    if (this.checked == false){
        document.body.className = 'lighttheme';
    }
});