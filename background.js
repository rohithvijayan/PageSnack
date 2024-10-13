
function getPageContent(){
    const pagecontent=document.body.pageContent
    const headings=Array.from(document.querySelectorAll('p')).map(heading => heading.innerText).join('\n');
    return headings;
}

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
        //const title=document.getElementById('title');
        const summaryDiv=document.getElementById("summary");        
        //title.innerText=data.title;
        const loading=document.getElementById("loading");

        function showLoader() {
            loading.style.display = 'contents'; // Display the loader immediately
          }
        function hideLoader() {
        loading.style.display = 'none'; // Hide the loader when summary is ready
        }
  
        var summarry=data.summary;
        function getSummarY(){
            summaryDiv.style.display ='none';
            summaryDiv.innerHTML=data.summary;
        }
        getSummarY();
        console.log(summarry);
        let summaryVisibility=false;
        const btn=document.getElementById('sum-btn');
        function displaySummary(){
            summaryDiv.style.display="contents";
            hideLoader();
        }
        btn.addEventListener("click",()=>{
            showLoader();
            if(!summaryVisibility){
                setTimeout(displaySummary,600);
                btn.innerText="Hide Summary";
                summaryVisibility=true;
                console.log("clicked");
            }   
        })
        btn.addEventListener("dblclick",()=>{ 
            summaryDiv.innerHTML="";
            btn.innerText="Summarize";
            hideLoader();
        })
        })
        .catch(error => {
        console.error('Error summarizing content:', error);
        });
    });
});