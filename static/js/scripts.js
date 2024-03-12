const sliderBtn = document.querySelector("#slider");
const styleCss = document.documentElement.style;
if (localStorage.getItem('sliderState')==='checked'){
    sliderBtn.checked = true;
    document.body.classList.add("dark-theme");
    
    
}


sliderBtn.addEventListener('change', function(){
  
    localStorage.setItem('sliderState', this.checked ? 'checked': 'unchecked');
    document.body.classList.toggle(("dark-theme"))
   
})


