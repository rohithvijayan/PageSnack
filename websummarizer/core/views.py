from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from groq import Groq
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    print("IT is there")
    print(request.data)
    if request.method=="POST" and 'content' in request.POST:
        content=request.POST['content']
        print(content)
    return HttpResponse("WORK AAYI BOISS")
    if request.method=='POST' and 'content' not in request.POST:
        print("IT is not there")
    if request.method=='GET':
        return JsonResponse({'title':"WebSummarizer"})
    else:
        pass
def summarizer(content):
    client=Groq(api_key="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")
    content_summary=client.chat.completions.create(messages=[{'role':'server','content':f'Summarize the content by identifying the [KEYWORDS] and main points, focusing on the most [CRUCIAL/IMPORTANT/EFFICIENT] information. Provide a concise summary in 3-5 points that answers the question(s): [MAIN QUESTIONS TO BE ANSWERED]. Please highlight the [KEY TAKEAWAYS/MAIN CONCEPTS] that a reader would need to know after reading the webpage.'}],model=)