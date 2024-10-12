from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from groq import Groq
import google.generativeai as genai
import os
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    #print("IT is there")
    #print("THIS IS LINE 2:::",request.data)
    if request.method=="POST":
        #print("ENTERED")
        content=request.data
        #print(content)
        summary=summarizer(content)
    return HttpResponse("data obtained")
    if request.method=='GET':
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
    summary=model.generate_content(f'I want you to act as a webpage summarizer. First, read the webpage thoroughly and identify the key ideas and themes. Then, follow these steps to generate a summary:Start by briefly identifying the main topic or purpose of the webpage.Focus on extracting the most important pieces of information or arguments, grouping related points together.For each topic, provide a clear and concise statement that captures the essence of the idea.Make sure the points are independent, and do not overlap with each other.Ensure that the summary is presented in the form of 3 to 6 key points.Avoid unnecessary details, focusing only on what is most relevant to the user.Present the points in a clean, plain-text format without any symbols, bullet points, or asterisks,there should be maximum of 2 detail for each point.Use plain text and follow this structure:{response_format}INPUT={content}').text
    print(summary)