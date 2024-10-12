function getPageContent() {
  return document.body.innerText; // Fetches all text from the page
}
document.addEventListener('DOMContentLoaded',function(){
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: () => document.body.innerText,
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
        const summaryElement = document.getElementById('summary');
        if (summaryElement) {
            summaryElement.textContent = data.summary;
        } else {
            console.error('Summary element not found');
        }
        })
        .catch(error => {
        console.error('Error summarizing content:', error);
        });
    });
})});