
function getPageContent(){return document.body.innerText;}
document.addEventListener('DOMContentLoaded',function(){
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: getPageContent,
    }, (results) => {
        const pageContent = results[0].result;
        fetch('http://127.0.0.1:8000/api/home/', {
        method: "POST",
        body: JSON.stringify({ content: pageContent }),
        headers: {
            'Content-Type': 'application/json',
        },
        })
        .then((response) => response.json())
        .then((data) => {
        const title=document.getElementById('title');
        const summaryDiv=document.getElementById("summary");
        const summaryElement = document.getElementById('summary-text');
        
        title.innerText=data.title
        const btn=document.getElementById('sum-btn')
        btn.addEventListener("click",()=>{
                summaryDiv.innerHTML = data.summary;
                console.log("clicked")

        })
        
        })
        .catch(error => {
        console.error('Error summarizing content:', error);
        });
    });
})});