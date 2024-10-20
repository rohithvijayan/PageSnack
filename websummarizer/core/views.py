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
	#print("POST CONTENT:",content)
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