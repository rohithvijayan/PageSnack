from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import google.generativeai as genai
import os
# Create your views here.
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
@api_view(['GET','POST'])
def home(request):
    #print("IT is there")
    #print("THIS IS LINE 2:::",request.data)
	#print("ENTERED")
	content=request.data.get('content')
	#print("POST CONTENT:",content)
	summary=summarizer(content)
	return JsonResponse({'title':"WebSummarizer",'summary':summary})


def summarizer(content):
    summary=model.generate_content(
    f""""
        Here's a tweaked version of your template prompt that focuses on brevity, ensuring a quick response and adding the required line breaks for clarity:
        Optimized Prompt for Quick Response: I want you to act as a webpage summarizer. Follow these steps to generate a very brief summary in HTML format:
        Analyze the Webpage: Identify the most important headlines or key ideas.Extract Core Information: Select 2 to 4 essential pieces of information that represent the main ideas.
        Format the Summary:
        Use <ul> for an unordered list.
        Use <li> for each title, and insert a <br> after each <li> for spacing.
        insert a <br> after each <li> for spacing
        Focus on Brevity: Keep the summary short and clear. Avoid unnecessary details.
        Strictly avoid using ```html in the response.
        Now, summarize the following webpage based on these steps.INPUT={content}
        """,safety_settings=None)
    print(summary.text)
    return summary.text

def quickResponse(selection):
    quick_Response=model.generate_content(f'''I want you to act as a Quick Search Engine. Follow these steps to generate a very brief Search Result in HTML format:
        Analyze the Input :If the input is a normal word Search for  the meaning,if the input is a person/place/event/thing search for and identify the most important and relevant details and information.Extract Core Information: Select 1 to 3 essential pieces of information that represent the main ideas.
        Format the Response:
        Use <ul> for an unordered list.
        Use <li> for each title, and insert a <br> after each <li> for spacing.
        insert a <br> after each <li> for spacing
        Focus on Brevity: Keep the summary short and clear. Avoid unnecessary details.
        Strictly avoid using ```html in the response.
        Now, Search the following item based on these steps.INPUT :{selection}
        ''')
    print(quick_Response.text)
    return quick_Response.text
@api_view(['POST', 'GET'])
def quick_search(request):  
    selection=request.data.get('selection')
    print("QUICK SEARCH:::",selection)
    response=quickResponse(selection)
    return JsonResponse({'quickSearch':response})

