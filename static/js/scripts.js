const sliderBtn = document.querySelector("#slider");
const styleCss = document.documentElement.style;
const menu = document.querySelector(".menu ion-icon");
const navBar = document.querySelector(".navBar");
const ul = document.querySelector('.navBar ul ');
const all_link = ul.querySelectorAll('a');
const span = ul.querySelectorAll('span');



if (localStorage.getItem('sliderState')==='checked'){
    sliderBtn.checked = true;
    document.body.classList.add("dark-theme");
    
    
}


sliderBtn.addEventListener('change', function(){
  
    localStorage.setItem('sliderState', this.checked ? 'checked': 'unchecked');
    document.body.classList.toggle(("dark-theme"));
   
});

 
menu.onclick = function(){
    navBar.classList.toggle("navBar-res");
    all_link.forEach((a)=>{
        a.classList.toggle('link');
    });
    span.forEach((sp)=>{
        sp.classList.toggle("span")
    })
    
}
var menuName = menu.getAttribute('name')
/* <ion-icon name="close-outline"></ion-icon> */
menu.addEventListener('click', ()=>{
    
   if(menu.getAttribute('name')==='menu-outline'){
    menu.setAttribute('name', 'close-outline');
    menu.style.transform = "translateX(400px)"
    menu.style.fontSize = "30px";
    
   }

   else{
   
    menu.setAttribute('name','menu-outline');
    menu.style.transform = "translateX(0)";
    
   };
   
});
    


