from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import google.generativeai as genai
import os
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    #print("IT is there")
    #print("THIS IS LINE 2:::",request.data)
	#print("ENTERED")
	content=request.data.get('content')
	#print(content)
	summary=summarizer(content)
	return JsonResponse({'title':"WebSummarizer",'summary':summary})


def summarizer(content):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response_format="""
    Response Example:
        1. Introduction to AI:
        - AI is a branch of computer science focused on creating intelligent systems.
        - It involves machine learning, natural language processing, and robotics.
        - AI has applications in various industries like healthcare, finance, and education.

        2. Types of Machine Learning:
        - Supervised, unsupervised, and reinforcement learning are the three main types.
        - Supervised learning relies on labeled data for training models.
        - Unsupervised learning is used when the data is not labeled, often for clustering.
        
        3. Challenges in AI Development:
        - Lack of transparency in decision-making processes.
        - Data bias can lead to unfair outcomes.
        - High computational costs and resource consumption are major barriers.

        4. Future of AI:
        - AI is expected to revolutionize industries like transportation and healthcare.
        - The rise of ethical AI is crucial for widespread adoption.
        - AI may lead to job automation, creating both opportunities and challenges.
        """
    summary=model.generate_content(f""""II want you to act as a webpage summarizer. Please follow these steps to generate a brief summary in HTML format:

Read the Webpage: Analyze the webpage content to identify the most important headlines or key ideas that encapsulate the main message.

Extract Core Information: Identify 2 to 4 essential pieces of information that provide context about the webpage. These should be concise and represent the core ideas.

Structure the Response: Format the summary in HTML using the following structure:

Create an unordered list with the <ul> tag.
Use the <li> tag for each title or heading to maintain clarity and organization.
Focus on Brevity: Avoid unnecessary details to ensure the summary is brief and clear.

Stricly Avoid ```html  in the response.

Finally, please summarize the following webpage, keeping these steps in mind.INPUT={content}""")
    print(summary.text)
    return summary.text