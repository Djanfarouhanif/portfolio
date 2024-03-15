const post  = document.querySelector(".post");
const projects = document.querySelector('.project-container');
const button = document.querySelectorAll(".project button");


button.forEach((b)=>{
    b.addEventListener('click', ()=>{
        projects.style.display = "none";
        post.style.display = "flex"
        
    })
});


post.addEventListener('click', ()=>{
   
    post.style.display = 'none';
    projects.style.display = 'flex';
})