from django.shortcuts import render
from .text_summary import summarize_text, analyze_sentiment

def home(request):
    return render(request, 'summarizer/home.html')

def summarize(request):
    if request.method == 'POST':
        input_text = request.POST.get('legal_text')
        summary = summarize_text(input_text)
        sentiment = analyze_sentiment(summary)
        return render(request, 'summarizer/result.html', {
            'original': input_text,
            'summary': summary,
            'sentiment': sentiment,
        })
    return render(request, 'summarizer/home.html')
