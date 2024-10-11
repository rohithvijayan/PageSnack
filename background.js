document.addEventListener("DOMContentLoaded",function(){
    const btn=document.getElementById("sum-btn");
    btn.addEventListener("click",function(){
        console.log("button clicked");
        const dummy=document.getElementsByClassName("dummy")[0];
        dummy.style.display="contents";
    })
    btn.addEventListener("dblclick",function(){
        console.log("double-clicked");
        const dummy=document.getElementsByClassName("dummy")[0];
        dummy.style.display="none";
    })
    

    setTimeout(() =>{
        fetch("http://127.0.0.1:8000//api/home/")
         .then(response => response.json())
         .then(data =>{
            document.getElementById('title').textContent=data.title;
         })
    })
});