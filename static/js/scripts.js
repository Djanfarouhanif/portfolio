const sliderBtn = document.querySelector("#slider");
const styleCss = document.documentElement.style
if (localStorage.getItem('sliderState')==='checked'){
    sliderBtn.checked = true;
    
}


sliderBtn.addEventListener('change', function(){
  
    localStorage.setItem('sliderState', this.checked ? 'checked': 'unchecked');
    console.log(localStorage.getItem('sliderState'));
   
})

